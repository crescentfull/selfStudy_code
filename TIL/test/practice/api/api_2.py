from dataclasses import dataclass


# ===== Domain Errors =====
class DomainError(Exception): ...


class InvalidCoupon(DomainError): ...


class BadQuantity(DomainError): ...


# ===== DTOs =====
@dataclass
class PlaceOrderCmd:
    user_id: str
    items: list  # [{ "sku": str, "qty": int, "price": int }]
    coupon_code: str | None = None
    idempotency_key: str | None = None


@dataclass
class OrderResult:
    order_id: str
    total_amount: int


# ===== Domain Rules =====
def assert_positive_qty(items):
    for it in items:
        if it["qty"] <= 0:
            raise BadQuantity("수량은 1 이상이어야 한다")


# ===== Infrastructure (In-Memory) =====
class InMemoryOrderRepo:
    def __init__(self):
        self._orders = {}
        self._auto = 1
        self.saves = 0  # 테스트용 계측

    def save(self, order_dict):
        order_id = str(self._auto)
        self._auto += 1
        self._orders[order_id] = order_dict | {"id": order_id}
        self.saves += 1
        return order_id

    def find_by_id(self, order_id):
        return self._orders.get(order_id)


class InMemoryCouponRepo:
    def __init__(self, coupons):
        # coupons 예: {"C10": {"percent": 10, "used": False}}
        self._coupons = coupons

    def get_active_for_update(self, code):
        c = self._coupons.get(code)
        if c and not c.get("used", False):
            return {"code": code, **c}
        return None

    def mark_used(self, coupon, order_id):
        self._coupons[coupon["code"]]["used"] = True


class InMemoryIdemStore:
    def __init__(self):
        self._store = {}

    def get(self, key):
        return self._store.get(key)

    def set(self, key, value, ttl_seconds=0):
        self._store[key] = value  # 데모: TTL 미적용(실전은 Redis 권장)


class PricingService:
    def sum_items(self, items):
        return sum(it["qty"] * it["price"] for it in items)

    def discount(self, subtotal, coupon):
        return subtotal * coupon["percent"] // 100


class UnitOfWork:
    def run(self, fn):
        # 데모: In-Memory라 트랜잭션 없음
        return fn()


# ===== Use Case =====
def place_order(cmd, order_repo, coupon_repo, pricing, uow, idem_store, clock=None):
    # 1) 멱등 체크
    if cmd.idempotency_key:
        cached = idem_store.get(cmd.idempotency_key)
        if cached:
            return cached

    def _work():
        # 2) 의미 검증
        assert_positive_qty(cmd.items)

        # 3) 가격 계산
        subtotal = pricing.sum_items(cmd.items)

        discount = 0
        if cmd.coupon_code:
            coupon = coupon_repo.get_active_for_update(cmd.coupon_code)
            if not coupon:
                raise InvalidCoupon("쿠폰이 유효하지 않다")
            discount = pricing.discount(subtotal, coupon)

        total = max(0, subtotal - discount)

        # 4) 저장 + 부수효과
        oid = order_repo.save(
            {
                "user_id": cmd.user_id,
                "items": cmd.items,
                "subtotal": subtotal,
                "discount": discount,
                "total": total,
            }
        )

        if cmd.coupon_code:
            coupon_repo.mark_used({"code": cmd.coupon_code}, oid)

        return OrderResult(order_id=oid, total_amount=total)

    result = uow.run(_work)

    # 5) 멱등 결과 캐시
    if cmd.idempotency_key:
        idem_store.set(cmd.idempotency_key, result)

    return result


# ===== Tests (pytest로도 동작) =====
def test_place_order_no_coupon():
    order_repo = InMemoryOrderRepo()
    coupon_repo = InMemoryCouponRepo({})
    idem = InMemoryIdemStore()
    pricing = PricingService()
    uow = UnitOfWork()

    cmd = PlaceOrderCmd(
        user_id="u1",
        items=[
            {"sku": "A", "qty": 2, "price": 1000},
            {"sku": "B", "qty": 1, "price": 5000},
        ],
    )
    res = place_order(cmd, order_repo, coupon_repo, pricing, uow, idem)
    assert res.total_amount == 7000
    assert order_repo.saves == 1


def test_place_order_with_coupon():
    order_repo = InMemoryOrderRepo()
    coupon_repo = InMemoryCouponRepo({"C10": {"percent": 10, "used": False}})
    idem = InMemoryIdemStore()
    pricing = PricingService()
    uow = UnitOfWork()

    cmd = PlaceOrderCmd(
        user_id="u1",
        items=[{"sku": "A", "qty": 1, "price": 10000}],
        coupon_code="C10",
    )
    res = place_order(cmd, order_repo, coupon_repo, pricing, uow, idem)
    assert res.total_amount == 9000
    assert coupon_repo._coupons["C10"]["used"] is True  # 쿠폰 사용 처리 확인


def test_invalid_quantity_raises():
    order_repo = InMemoryOrderRepo()
    coupon_repo = InMemoryCouponRepo({})
    idem = InMemoryIdemStore()
    pricing = PricingService()
    uow = UnitOfWork()

    cmd = PlaceOrderCmd(
        user_id="u1",
        items=[{"sku": "A", "qty": 0, "price": 1000}],
    )
    raised = False
    try:
        place_order(cmd, order_repo, coupon_repo, pricing, uow, idem)
    except BadQuantity:
        raised = True
    assert raised


def test_idempotent_two_calls_one_save():
    order_repo = InMemoryOrderRepo()
    coupon_repo = InMemoryCouponRepo({})
    idem = InMemoryIdemStore()
    pricing = PricingService()
    uow = UnitOfWork()

    cmd = PlaceOrderCmd(
        user_id="u1",
        items=[{"sku": "A", "qty": 1, "price": 1000}],
        idempotency_key="idem-1",
    )
    res1 = place_order(cmd, order_repo, coupon_repo, pricing, uow, idem)
    res2 = place_order(cmd, order_repo, coupon_repo, pricing, uow, idem)
    assert res1.order_id == res2.order_id
    assert order_repo.saves == 1  # 멱등으로 저장 1회만 발생


# ===== Built-in test runner (pytest 없이도 실행 가능) =====
def _run_builtin_tests():
    tests = [
        test_place_order_no_coupon,
        test_place_order_with_coupon,
        test_invalid_quantity_raises,
        test_idempotent_two_calls_one_save,
    ]
    for t in tests:
        t()
    print("✅ All tests passed.")


if __name__ == "__main__":
    _run_builtin_tests()
