\*\*“쿠폰 발급·사용 API”\*\*를 주제로 설계 연습을 해보자.
이 도메인은 **멱등성(Idempotency), 동시성, 상태 전이, 페이지네이션, 검증 규칙**까지 한 번에 연습하기 좋다.

# 무엇을 연습하나

* POST 멱등성(중복 발급 방지) — `Idempotency-Key` 헤더
* 상태 전이(issued → redeemed → cancelled/expired)
* 동시성 안전한 사용(중복 사용 방지)
* 커서 기반 페이지네이션/필터/정렬
* 표준 에러 포맷과 코드 설계

---

# 요구사항 (요약)

1. 운영자는 **쿠폰 배치**를 만든다(정액/정률, 만료일, 발급 한도).
2. 유저는 **쿠폰 발급**을 요청한다(배치 기준 규칙 체크, 1인 발급 제한 등).
3. 유저(또는 주문시스템)는 **쿠폰 사용(=차감 적용)** 을 요청한다.
4. 동일 요청 재시도 시 **중복 발급/중복 사용이 절대 발생하면 안 됨**(네트워크 재시도 대비).
5. 모든 쓰기 요청은 **멱등성 키**를 받아야 한다.

---

# 리소스 & 모델

## CouponBatch

* `id` (PK)
* `name` (str)
* `discount_type` (`fixed`, `percent`)
* `amount` (int) / `percent` (0\~100)
* `per_user_limit` (int, default 1)
* `total_limit` (int, 전체 발급 최대 수)
* `expires_at` (datetime)
* `created_at`/`updated_at`

## Coupon

* `id` (PK)
* `batch_id` (FK)
* `code` (unique, 대문자+숫자 10자)
* `issued_to` (user\_id, nullable)
* `issued_at`
* `status` (`issued`, `redeemed`, `cancelled`, `expired`)
* `redeemed_by` (user\_id, nullable)
* `redeemed_at`
* `order_id` (nullable)
* 인덱스: `(code)`, `(issued_to,status)`, `(batch_id,status)`

## IdempotencyKey (쓰기 요청 전용)

* `key` (unique)
* `request_hash` (선택: body 요약)
* `response_status`/`response_body` (저장)
* `user_id` (요청자)
* `created_at`, `expires_at` (예: 24h)

---

# API 설계 (v1)

## 인증

* `Authorization: Bearer <token>`

## 공통 에러 포맷

```json
{
  "error": {
    "code": "COUPON_ALREADY_REDEEMED",
    "message": "Coupon already redeemed",
    "details": { "code": "AB12..." }
  }
}
```

## 1) 배치 생성 (운영자)

`POST /v1/coupon-batches`
Headers: `Idempotency-Key: <uuid>`

Request

```json
{
  "name": "Welcome 10%",
  "discount_type": "percent",
  "percent": 10,
  "per_user_limit": 1,
  "total_limit": 10000,
  "expires_at": "2026-12-31T23:59:59Z"
}
```

201 Created

```json
{ "id": "bat_123", "name": "Welcome 10%", "discount_type": "percent", ... }
```

## 2) 쿠폰 발급

`POST /v1/coupons/issue`
Headers: `Idempotency-Key: <uuid>`

Request

```json
{ "batch_id": "bat_123" }
```

200 OK

```json
{
  "id": "cpn_456",
  "code": "A2K7X9Q1ZP",
  "status": "issued",
  "issued_to": "user_42",
  "expires_at": "2026-12-31T23:59:59Z"
}
```

에러 예:

* 400 `BATCH_EXPIRED`
* 409 `PER_USER_LIMIT_REACHED`
* 409 `BATCH_LIMIT_REACHED`

> 멱등성: 같은 헤더/같은 본문으로 재시도 시 **항상 같은 응답**.

## 3) 쿠폰 사용(차감)

`POST /v1/coupons/redeem`
Headers: `Idempotency-Key: <uuid>`

Request

```json
{
  "code": "A2K7X9Q1ZP",
  "order_id": "ord_20250810_0001"
}
```

200 OK

```json
{
  "code": "A2K7X9Q1ZP",
  "status": "redeemed",
  "redeemed_at": "2025-08-10T07:12:10Z",
  "order_id": "ord_20250810_0001",
  "discount_applied": { "type": "percent", "value": 10 }
}
```

에러 예:

* 404 `COUPON_NOT_FOUND`
* 409 `COUPON_ALREADY_REDEEMED`
* 410 `COUPON_EXPIRED`
* 403 `COUPON_OWNERSHIP_MISMATCH` (본인 것만 사용 가능 정책일 때)

> **동시성**: 같은 코드로 두 요청이 동시에 오면 **한 쪽만 성공, 다른 쪽은 409**.

## 4) 쿠폰 조회(리스트)

`GET /v1/coupons?status=issued&user_id=me&limit=20&cursor=eyJpZCI6...`
200 OK

```json
{
  "items": [
    { "code": "A2K7...", "status": "issued", "expires_at": "...", ... }
  ],
  "next_cursor": "eyJpZCI6..."
}
```

* 커서 기반(역정렬: 최신 발급 먼저), `next_cursor` 없으면 마지막.

## 5) 쿠폰 취소 (운영자/혹은 유저)

`PATCH /v1/coupons/{code}`
Headers: `If-Match: "<rev>"` (낙관적 락, 선택)
Body

```json
{ "status": "cancelled", "reason": "user_request" }
```

---

# 핵심 규칙

* **만료**: `expires_at` 기준 자동 만료 처리(조회 시 상태 계산 또는 배치 잡)
* **퍼센트/정액**: 서로 배타적. 서버에서 한쪽만 허용.
* **한도**: `per_user_limit`, `total_limit` 모두 초과 불가.
* **멱등성**: `Idempotency-Key` 필수(POST/PUT/PATCH). 같은 키로 24h 내 재요청 → **동일 응답 반환**.

---

# 테스트 시나리오 (필수)

1. 동일 발급 요청 2번(같은 Idempotency-Key) → **완전 동일 응답**
2. Idempotency-Key 없이 같은 본문 2번 → **서로 다른 쿠폰**(정상)
3. 만료 배치 발급 시도 → 400 `BATCH_EXPIRED`
4. per\_user\_limit=1인 배치에서 같은 유저 2회 발급 → 첫 성공, 두 번째 409
5. 동일 코드로 동시에 사용 요청(멀티 스레드/프로세스) → 한쪽 200, 한쪽 409
6. 커서 페이지네이션: limit=2로 5개 순회 시 3페이지로 모두 회수됨 확인

---

# (선택) Django REST Framework 코드 스켈레톤

> 최신 스타일 위주. 상세 구현은 짧게 핵심만.

**models.py**

```python
from django.db import models
from django.utils import timezone

class CouponBatch(models.Model):
    DISCOUNT_FIXED = "fixed"
    DISCOUNT_PERCENT = "percent"
    DISCOUNT_CHOICES = [(DISCOUNT_FIXED,"fixed"), (DISCOUNT_PERCENT,"percent")]

    name = models.CharField(max_length=80)
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_CHOICES)
    amount = models.IntegerField(null=True, blank=True)     # fixed용
    percent = models.IntegerField(null=True, blank=True)    # percent용 (0~100)
    per_user_limit = models.IntegerField(default=1)
    total_limit = models.IntegerField()
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Coupon(models.Model):
    STATUS_ISSUED = "issued"
    STATUS_REDEEMED = "redeemed"
    STATUS_CANCELLED = "cancelled"
    STATUS_EXPIRED = "expired"
    STATUS_CHOICES = [(STATUS_ISSUED,"issued"), (STATUS_REDEEMED,"redeemed"),
                      (STATUS_CANCELLED,"cancelled"), (STATUS_EXPIRED,"expired")]
    batch = models.ForeignKey(CouponBatch, on_delete=models.PROTECT)
    code = models.CharField(max_length=16, unique=True)
    issued_to = models.CharField(max_length=64, null=True, blank=True)  # user_id
    issued_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_ISSUED)
    redeemed_by = models.CharField(max_length=64, null=True, blank=True)
    redeemed_at = models.DateTimeField(null=True, blank=True)
    order_id = models.CharField(max_length=64, null=True, blank=True)

class IdempotencyKey(models.Model):
    key = models.CharField(max_length=64, unique=True)
    user_id = models.CharField(max_length=64)
    request_fingerprint = models.CharField(max_length=128, null=True, blank=True)
    response_status = models.IntegerField(null=True, blank=True)
    response_body = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=lambda: timezone.now() + timezone.timedelta(hours=24))
```

**서비스 로직 (트랜잭션 + select\_for\_update)**

```python
from django.db import transaction
from django.utils import timezone

def redeem_coupon(code: str, user_id: str, order_id: str) -> dict:
    from .models import Coupon
    with transaction.atomic():
        # 행 잠금으로 동시성 제어
        coupon = Coupon.objects.select_for_update().get(code=code)
        # 만료 체크
        if coupon.batch.expires_at < timezone.now():
            raise ValueError("COUPON_EXPIRED")
        if coupon.status == Coupon.STATUS_REDEEMED:
            raise ValueError("COUPON_ALREADY_REDEEMED")
        coupon.status = Coupon.STATUS_REDEEMED
        coupon.redeemed_by = user_id
        coupon.redeemed_at = timezone.now()
        coupon.order_id = order_id
        coupon.save(update_fields=["status","redeemed_by","redeemed_at","order_id"])
    # 할인 정보 계산 응답(예시)
    discount = {"type": coupon.batch.discount_type,
                "value": coupon.batch.percent if coupon.batch.discount_type=="percent" else coupon.batch.amount}
    return {"code": coupon.code, "status": coupon.status, "order_id": coupon.order_id,
            "redeemed_at": coupon.redeemed_at.isoformat(), "discount_applied": discount}
```

**멱등성 처리 (뷰 데코레이터 개념)**

```python
from functools import wraps
from django.http import JsonResponse
from .models import IdempotencyKey
from django.utils import timezone

def idempotent_view(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        key = request.headers.get("Idempotency-Key")
        if not key:  # 정책: 필수
            return JsonResponse({"error":{"code":"IDEMPOTENCY_KEY_REQUIRED","message":"Provide Idempotency-Key"}}, status=400)
        ik = IdempotencyKey.objects.filter(key=key).first()
        if ik:
            return JsonResponse(ik.response_body, status=ik.response_status)
        # 최초 처리
        response = func(request, *args, **kwargs)
        # 응답 저장
        IdempotencyKey.objects.create(
            key=key, user_id=str(request.user.id),
            response_status=response.status_code,
            response_body=getattr(response, "data", None) or {}
        )
        return response
    return wrapper
```

> 실제 DRF에선 `APIView`/`GenericViewSet`에 Mixin으로 붙이는 편이 깔끔하다.

---

# 체크리스트 (스스로 평가)

* [ ] 쓰기 요청에 `Idempotency-Key` 없으면 400
* [ ] 같은 키로 재시도 시 본문이 달라도? → 409 `IDEMPOTENCY_KEY_BODY_MISMATCH` (선택)
* [ ] `select_for_update`로 이중 사용 레이스에서 정확히 한 요청만 성공
* [ ] 배치/쿠폰 만료 로직 일관성(조회 vs 잡)
* [ ] 커서 페이지네이션: stable sort key 사용(id 또는 (created\_at,id))
* [ ] 에러 코드가 구체적이고, 클라이언트가 분기 처리 가능

---

필요하면 위 설계를 **실행 가능한 DRF 프로젝트 뼈대 + pytest API 테스트**로 바로 만들어 줄게.
다음 주제 후보: **주문·결제 API(부분 환불/멀티 통화/서킷브레이커)**, **태그 기반 노트 API(검색·정렬·공유)** — 원하는 걸 고르면 그걸로 이어서!
