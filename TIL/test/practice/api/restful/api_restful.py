from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum
import uuid

from fastapi import FastAPI, HTTPException, Depends, status, Header
from pydantic import BaseModel, Field, validator
from fastapi.responses import JSONResponse


# ===== Domain Errors =====
class DomainError(Exception):
    def __init__(self, message: str, error_code: str = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code or self.__class__.__name__


class InvalidCoupon(DomainError):
    def __init__(self, coupon_code: str):
        super().__init__(
            f"쿠폰이 유효하지 않습니다: {coupon_code}", error_code="INVALID_COUPON"
        )
        self.coupon_code = coupon_code


class BadQuantity(DomainError):
    def __init__(self, qty: int, item_sku: str = None):
        msg = f"수량은 1 이상이어야 합니다. 입력값: {qty}"
        if item_sku:
            msg += f" (상품: {item_sku})"
        super().__init__(msg, error_code="INVALID_QUANTITY")
        self.qty = qty
        self.item_sku = item_sku


class OrderNotFound(DomainError):
    def __init__(self, order_id: str):
        super().__init__(
            f"주문을 찾을 수 없습니다: {order_id}", error_code="ORDER_NOT_FOUND"
        )
        self.order_id = order_id


# ===== Pydantic Models (Request/Response) =====
class OrderItem(BaseModel):
    sku: str = Field(..., description="상품 코드", example="ITEM001")
    qty: int = Field(..., gt=0, description="수량 (1 이상)", example=2)
    price: int = Field(..., gt=0, description="단가 (원)", example=10000)

    class Config:
        json_schema_extra = {"example": {"sku": "ITEM001", "qty": 2, "price": 10000}}


class CreateOrderRequest(BaseModel):
    user_id: str = Field(..., description="사용자 ID", example="user123")
    items: List[OrderItem] = Field(..., min_items=1, description="주문 상품 목록")
    coupon_code: Optional[str] = Field(
        None, description="쿠폰 코드", example="DISCOUNT10"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user123",
                "items": [
                    {"sku": "ITEM001", "qty": 2, "price": 10000},
                    {"sku": "ITEM002", "qty": 1, "price": 5000},
                ],
                "coupon_code": "DISCOUNT10",
            }
        }


class OrderResponse(BaseModel):
    order_id: str = Field(..., description="주문 ID")
    user_id: str = Field(..., description="사용자 ID")
    items: List[OrderItem] = Field(..., description="주문 상품 목록")
    subtotal: int = Field(..., description="소계 (원)")
    discount: int = Field(..., description="할인 금액 (원)")
    total: int = Field(..., description="최종 금액 (원)")
    coupon_code: Optional[str] = Field(None, description="사용된 쿠폰 코드")
    created_at: datetime = Field(..., description="주문 생성 시간")

    class Config:
        json_schema_extra = {
            "example": {
                "order_id": "ORD123456",
                "user_id": "user123",
                "items": [{"sku": "ITEM001", "qty": 2, "price": 10000}],
                "subtotal": 20000,
                "discount": 2000,
                "total": 18000,
                "coupon_code": "DISCOUNT10",
                "created_at": "2023-12-01T10:30:00Z",
            }
        }


class CouponResponse(BaseModel):
    code: str = Field(..., description="쿠폰 코드")
    percent: int = Field(..., description="할인율 (%)")
    is_used: bool = Field(..., description="사용 여부")

    class Config:
        json_schema_extra = {
            "example": {"code": "DISCOUNT10", "percent": 10, "is_used": False}
        }


class ErrorResponse(BaseModel):
    error_code: str = Field(..., description="에러 코드")
    message: str = Field(..., description="에러 메시지")
    details: Optional[Dict[str, Any]] = Field(None, description="상세 정보")

    class Config:
        json_schema_extra = {
            "example": {
                "error_code": "INVALID_QUANTITY",
                "message": "수량은 1 이상이어야 합니다",
                "details": {"field": "items[0].qty", "value": 0},
            }
        }


# ===== Infrastructure (동일한 로직 재사용) =====
class InMemoryOrderRepo:
    def __init__(self):
        self._orders = {}
        self._auto = 1

    def save(self, order_dict):
        order_id = f"ORD{str(self._auto).zfill(6)}"
        self._auto += 1
        order_dict["id"] = order_id
        order_dict["created_at"] = datetime.now()
        self._orders[order_id] = order_dict
        return order_id

    def find_by_id(self, order_id):
        return self._orders.get(order_id)


class InMemoryCouponRepo:
    def __init__(self, coupons):
        self._coupons = coupons

    def get_active_for_update(self, code):
        c = self._coupons.get(code)
        if c and not c.get("used", False):
            return {"code": code, **c}
        return None

    def mark_used(self, coupon, order_id):
        self._coupons[coupon["code"]]["used"] = True

    def find_by_code(self, code):
        c = self._coupons.get(code)
        if c:
            return {"code": code, **c}
        return None


class InMemoryIdemStore:
    def __init__(self):
        self._store = {}

    def get(self, key):
        return self._store.get(key)

    def set(self, key, value, ttl_seconds=0):
        self._store[key] = value


class PricingService:
    def sum_items(self, items):
        return sum(item.qty * item.price for item in items)

    def discount(self, subtotal, coupon):
        return subtotal * coupon["percent"] // 100


class UnitOfWork:
    def run(self, fn):
        return fn()


# ===== Dependency Injection =====
# 글로벌 인스턴스 (실제로는 DI 컨테이너 사용 권장)
order_repo = InMemoryOrderRepo()
coupon_repo = InMemoryCouponRepo(
    {
        "DISCOUNT10": {"percent": 10, "used": False},
        "DISCOUNT20": {"percent": 20, "used": False},
        "USED_COUPON": {"percent": 15, "used": True},
    }
)
idem_store = InMemoryIdemStore()
pricing_service = PricingService()
uow = UnitOfWork()


def get_order_repo():
    return order_repo


def get_coupon_repo():
    return coupon_repo


def get_idem_store():
    return idem_store


def get_pricing_service():
    return pricing_service


def get_uow():
    return uow


# ===== Use Case (수정된 버전) =====
def assert_positive_qty(items: List[OrderItem]):
    for item in items:
        if item.qty <= 0:
            raise BadQuantity(item.qty, item.sku)


def place_order_use_case(
    request: CreateOrderRequest,
    idempotency_key: Optional[str],
    order_repo: InMemoryOrderRepo,
    coupon_repo: InMemoryCouponRepo,
    pricing: PricingService,
    uow: UnitOfWork,
    idem_store: InMemoryIdemStore,
):
    # 멱등성 체크
    if idempotency_key:
        cached = idem_store.get(idempotency_key)
        if cached:
            return cached

    def _work():
        # 비즈니스 규칙 검증
        assert_positive_qty(request.items)

        # 가격 계산
        subtotal = pricing.sum_items(request.items)

        discount = 0
        if request.coupon_code:
            coupon = coupon_repo.get_active_for_update(request.coupon_code)
            if not coupon:
                raise InvalidCoupon(request.coupon_code)
            discount = pricing.discount(subtotal, coupon)

        total = max(0, subtotal - discount)

        # 주문 저장
        order_data = {
            "user_id": request.user_id,
            "items": [item.dict() for item in request.items],
            "subtotal": subtotal,
            "discount": discount,
            "total": total,
            "coupon_code": request.coupon_code,
        }

        order_id = order_repo.save(order_data)

        # 쿠폰 사용 처리
        if request.coupon_code:
            coupon_repo.mark_used({"code": request.coupon_code}, order_id)

        # 응답 객체 생성
        saved_order = order_repo.find_by_id(order_id)
        return OrderResponse(
            order_id=order_id,
            user_id=saved_order["user_id"],
            items=[OrderItem(**item) for item in saved_order["items"]],
            subtotal=saved_order["subtotal"],
            discount=saved_order["discount"],
            total=saved_order["total"],
            coupon_code=saved_order.get("coupon_code"),
            created_at=saved_order["created_at"],
        )

    result = uow.run(_work)

    # 멱등성 캐시
    if idempotency_key:
        idem_store.set(idempotency_key, result)

    return result


# ===== FastAPI Application =====
app = FastAPI(
    title="주문 처리 API",
    description="RESTful 주문 처리 시스템",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


# ===== Error Handlers =====
@app.exception_handler(DomainError)
async def domain_error_handler(request, exc: DomainError):
    status_code = status.HTTP_400_BAD_REQUEST
    if isinstance(exc, OrderNotFound):
        status_code = status.HTTP_404_NOT_FOUND

    return JSONResponse(
        status_code=status_code,
        content={
            "error_code": exc.error_code,
            "message": exc.message,
            "details": getattr(exc, "__dict__", {}),
        },
    )


@app.exception_handler(ValueError)
async def validation_error_handler(request, exc: ValueError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error_code": "VALIDATION_ERROR",
            "message": str(exc),
            "details": None,
        },
    )


# ===== API Endpoints =====
@app.post(
    "/orders",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
    summary="주문 생성",
    description="새로운 주문을 생성합니다. 멱등성 키를 사용하여 중복 생성을 방지할 수 있습니다.",
    responses={
        201: {"description": "주문 생성 성공"},
        400: {"model": ErrorResponse, "description": "잘못된 요청"},
        422: {"description": "입력 검증 실패"},
    },
)
async def create_order(
    request: CreateOrderRequest,
    idempotency_key: Optional[str] = Header(None, alias="Idempotency-Key"),
    order_repo: InMemoryOrderRepo = Depends(get_order_repo),
    coupon_repo: InMemoryCouponRepo = Depends(get_coupon_repo),
    pricing: PricingService = Depends(get_pricing_service),
    uow: UnitOfWork = Depends(get_uow),
    idem_store: InMemoryIdemStore = Depends(get_idem_store),
):
    """
    주문을 생성합니다.

    - **user_id**: 사용자 식별자
    - **items**: 주문할 상품 목록 (최소 1개)
    - **coupon_code**: 선택적 쿠폰 코드
    - **Idempotency-Key**: 중복 처리 방지를 위한 헤더 (선택사항)
    """
    return place_order_use_case(
        request, idempotency_key, order_repo, coupon_repo, pricing, uow, idem_store
    )


@app.get(
    "/orders/{order_id}",
    response_model=OrderResponse,
    summary="주문 조회",
    description="주문 ID로 주문 정보를 조회합니다.",
    responses={
        200: {"description": "주문 조회 성공"},
        404: {"model": ErrorResponse, "description": "주문을 찾을 수 없음"},
    },
)
async def get_order(
    order_id: str, order_repo: InMemoryOrderRepo = Depends(get_order_repo)
):
    """주문 ID로 주문 정보를 조회합니다."""
    order = order_repo.find_by_id(order_id)
    if not order:
        raise OrderNotFound(order_id)

    return OrderResponse(
        order_id=order["id"],
        user_id=order["user_id"],
        items=[OrderItem(**item) for item in order["items"]],
        subtotal=order["subtotal"],
        discount=order["discount"],
        total=order["total"],
        coupon_code=order.get("coupon_code"),
        created_at=order["created_at"],
    )


@app.get(
    "/coupons/{coupon_code}",
    response_model=CouponResponse,
    summary="쿠폰 조회",
    description="쿠폰 코드로 쿠폰 정보를 조회합니다.",
    responses={
        200: {"description": "쿠폰 조회 성공"},
        404: {"model": ErrorResponse, "description": "쿠폰을 찾을 수 없음"},
    },
)
async def get_coupon(
    coupon_code: str, coupon_repo: InMemoryCouponRepo = Depends(get_coupon_repo)
):
    """쿠폰 코드로 쿠폰 정보를 조회합니다."""
    coupon = coupon_repo.find_by_code(coupon_code)
    if not coupon:
        raise InvalidCoupon(coupon_code)

    return CouponResponse(
        code=coupon["code"],
        percent=coupon["percent"],
        is_used=coupon.get("used", False),
    )


@app.post(
    "/coupons/{coupon_code}/validate",
    response_model=CouponResponse,
    summary="쿠폰 검증",
    description="쿠폰이 사용 가능한지 검증합니다.",
    responses={
        200: {"description": "사용 가능한 쿠폰"},
        400: {"model": ErrorResponse, "description": "사용할 수 없는 쿠폰"},
    },
)
async def validate_coupon(
    coupon_code: str, coupon_repo: InMemoryCouponRepo = Depends(get_coupon_repo)
):
    """쿠폰이 사용 가능한지 검증합니다."""
    coupon = coupon_repo.get_active_for_update(coupon_code)
    if not coupon:
        raise InvalidCoupon(coupon_code)

    return CouponResponse(code=coupon["code"], percent=coupon["percent"], is_used=False)


@app.get("/health", summary="헬스체크", description="API 서버의 상태를 확인합니다.")
async def health_check():
    """API 서버의 상태를 확인합니다."""
    return {"status": "healthy", "timestamp": datetime.now()}


# ===== 개발용 실행 =====
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api_restful:app", host="0.0.0.0", port=8000, reload=True)
