from datetime import datetime, timezone
import hashlib, json, uuid
from typing import Optional, Literal, List

from fastapi import FastAPI, HTTPException, Depends, Header, Request, status, Query
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, field_validator
from sqlalchemy import String, Integer, DateTime, Boolean, Text, UniqueConstraint, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, sessionmaker

# -----------------------------
# DB & ORM (SQLAlchemy 2.0)
# -----------------------------
class Base(DeclarativeBase):
    pass

class Coupon(Base):
    __tablename__ = "coupons"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    discount_type: Mapped[str] = mapped_column(String(16))  # "fixed" | "percent"
    amount: Mapped[int] = mapped_column(Integer)            # 정액이면 금액, 정률이면 %
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    # 사용 정보
    redeemed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    redeemed_by: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)

class IdemRecord(Base):
    """
    간단한 Idempotency 저장소:
    - 동일한 key가 같은 payload로 재호출되면 stored_response를 그대로 반환
    - 같은 key인데 payload가 다르면 409
    """
    __tablename__ = "idempotency_keys"
    key: Mapped[str] = mapped_column(String(128), primary_key=True)
    method: Mapped[str] = mapped_column(String(8))
    path: Mapped[str] = mapped_column(String(256))
    body_hash: Mapped[str] = mapped_column(String(64))  # sha256
    status_code: Mapped[int] = mapped_column(Integer)
    stored_response: Mapped[str] = mapped_column(Text)  # JSON 문자열
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    __table_args__ = (UniqueConstraint("key", name="uq_idem_key"),)

engine = create_engine("sqlite:///./coupons.db", echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)
Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------
# Pydantic Schemas (v2)
# -----------------------------
class CouponCreate(BaseModel):
    code: Optional[str] = Field(None, description="지정하지 않으면 서버가 UUID 기반으로 생성")
    discount_type: Literal["fixed", "percent"]
    amount: int = Field(..., ge=1)
    expires_at: Optional[datetime] = None

    @field_validator("amount")
    def validate_amount(v, info):
        # percent면 1~100, fixed면 양수 금액으로 가이드
        discount_type = info.data.get("discount_type")
        if discount_type == "percent":
            if v < 1 or v > 100:
                raise ValueError("percent 할인은 1~100 사이여야 함")
        return v

class CouponOut(BaseModel):
    code: str
    discount_type: str
    amount: int
    is_active: bool
    created_at: datetime
    expires_at: Optional[datetime]
    redeemed_at: Optional[datetime]
    redeemed_by: Optional[str]

class RedeemRequest(BaseModel):
    code: str
    user_id: str

class RedeemResult(BaseModel):
    code: str
    redeemed_by: str
    redeemed_at: datetime

# -----------------------------
# Helpers
# -----------------------------
def now_utc():
    return datetime.now(timezone.utc)

def json_hash(payload_dict):
    body = json.dumps(payload_dict, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(body.encode("utf-8")).hexdigest()

def idem_get_or_set(db, key, method, path, body_dict, status_code=None, response_obj=None):
    """
    - 조회 시: 저장된 key가 있으면 payload 비교 후 그대로 재생
    - 저장 시: status_code와 response_obj를 함께 보관
    반환:
      (replayed: bool, status_code: int|None, response_obj: dict|None)
    """
    body_sha = json_hash(body_dict)
    rec = db.get(IdemRecord, key)
    if rec:
        if rec.method != method or rec.path != path or rec.body_hash != body_sha:
            raise HTTPException(status_code=409, detail="Idempotency-Key 재사용 충돌: payload 불일치")
        return True, rec.status_code, json.loads(rec.stored_response)

    if status_code is not None and response_obj is not None:
        rec = IdemRecord(
            key=key,
            method=method,
            path=path,
            body_hash=body_sha,
            status_code=status_code,
            stored_response=json.dumps(jsonable_encoder(response_obj), separators=(",", ":"), ensure_ascii=False),
        )
        db.add(rec)
        db.commit()
        return False, status_code, response_obj

    return False, None, None

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(title="Coupon Registration API", version="1.0")

# 루트 헬스체크
@app.get("/")
def health():
    return {"ok": True, "ts": now_utc().isoformat()}

# 쿠폰 등록
@app.post("/v1/coupons", response_model=CouponOut, status_code=status.HTTP_201_CREATED)
def create_coupon(
    payload: CouponCreate,
    db: Session = Depends(get_db),
    request: Request = None,
    idempotency_key: Optional[str] = Header(default=None, alias="Idempotency-Key"),
):
    body_dict = payload.model_dump()
    if idempotency_key:
        replayed, sc, saved = idem_get_or_set(db, idempotency_key, "POST", str(request.url.path), body_dict)
        if replayed:
            # 201로 저장했던 응답을 그대로 재생
            return saved

    code = payload.code or uuid.uuid4().hex[:10].upper()
    # 중복 코드 방지
    exists = db.scalar(select(Coupon).where(Coupon.code == code))
    if exists:
        raise HTTPException(status_code=409, detail="이미 존재하는 쿠폰 코드")

    coupon = Coupon(
        code=code,
        discount_type=payload.discount_type,
        amount=payload.amount,
        is_active=True,
        created_at=now_utc(),
        expires_at=payload.expires_at,
    )
    db.add(coupon)
    db.commit()
    db.refresh(coupon)

    out = CouponOut(
        code=coupon.code,
        discount_type=coupon.discount_type,
        amount=coupon.amount,
        is_active=coupon.is_active,
        created_at=coupon.created_at,
        expires_at=coupon.expires_at,
        redeemed_at=coupon.redeemed_at,
        redeemed_by=coupon.redeemed_by,
    )
    if idempotency_key:
        idem_get_or_set(db, idempotency_key, "POST", str(request.url.path), body_dict, status_code=201, response_obj=out.model_dump())
    return out

# 쿠폰 목록
@app.get("/v1/coupons", response_model=List[CouponOut])
def list_coupons(
    only_active: bool = Query(default=False),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
):
    stmt = select(Coupon).order_by(Coupon.created_at.desc()).limit(limit).offset(offset)
    if only_active:
        stmt = select(Coupon).where(Coupon.is_active == True).order_by(Coupon.created_at.desc()).limit(limit).offset(offset)  # noqa: E712

    rows = db.scalars(stmt).all()
    return [
        CouponOut(
            code=r.code,
            discount_type=r.discount_type,
            amount=r.amount,
            is_active=r.is_active,
            created_at=r.created_at,
            expires_at=r.expires_at,
            redeemed_at=r.redeemed_at,
            redeemed_by=r.redeemed_by,
        )
        for r in rows
    ]

# 단건 조회
@app.get("/v1/coupons/{code}", response_model=CouponOut)
def get_coupon(code: str, db: Session = Depends(get_db)):
    row = db.scalar(select(Coupon).where(Coupon.code == code))
    if not row:
        raise HTTPException(status_code=404, detail="쿠폰을 찾을 수 없음")
    return CouponOut(
        code=row.code,
        discount_type=row.discount_type,
        amount=row.amount,
        is_active=row.is_active,
        created_at=row.created_at,
        expires_at=row.expires_at,
        redeemed_at=row.redeemed_at,
        redeemed_by=row.redeemed_by,
    )

# 쿠폰 사용(등록코드 입력)
@app.post("/v1/coupons/redeem", response_model=RedeemResult)
def redeem(payload: RedeemRequest,
          db: Session = Depends(get_db),
          request: Request = None,
          idempotency_key: Optional[str] = Header(default=None, alias="Idempotency-Key")):
    body_dict = payload.model_dump()
    if idempotency_key:
        replayed, sc, saved = idem_get_or_set(db, idempotency_key, "POST", str(request.url.path), body_dict)
        if replayed:
            return saved

    row = db.scalar(select(Coupon).where(Coupon.code == payload.code))
    if not row:
        raise HTTPException(status_code=404, detail="쿠폰을 찾을 수 없음")
    if not row.is_active:
        raise HTTPException(status_code=400, detail="비활성화된 쿠폰")
    if row.expires_at and row.expires_at < now_utc():
        raise HTTPException(status_code=400, detail="만료된 쿠폰")
    if row.redeemed_at is not None:
        raise HTTPException(status_code=409, detail="이미 사용된 쿠폰")

    row.redeemed_by = payload.user_id
    row.redeemed_at = now_utc()
    db.add(row)
    db.commit()
    db.refresh(row)

    out = RedeemResult(code=row.code, redeemed_by=row.redeemed_by, redeemed_at=row.redeemed_at)
    if idempotency_key:
        idem_get_or_set(db, idempotency_key, "POST", str(request.url.path), body_dict, status_code=200, response_obj=out.model_dump())
    return out

# (선택) 쿠폰 비활성화
@app.delete("/v1/coupons/{code}", status_code=204)
def deactivate_coupon(code: str, db: Session = Depends(get_db)):
    row = db.scalar(select(Coupon).where(Coupon.code == code))
    if not row:
        raise HTTPException(status_code=404, detail="쿠폰을 찾을 수 없음")
    row.is_active = False
    db.add(row)
    db.commit()
    return
