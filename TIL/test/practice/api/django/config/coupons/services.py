import secrets, string
from django.db import transaction
from django.utils import timezone
from .models import Coupon, CouponBatch

CODE_ALPHABET = string.ascii_uppercase + string.digits


def _gen_code(length: int = 10) -> str:
    return "".join(secrets.choice(CODE_ALPHABET) for _ in range(length))


@transaction.atomic
def issue_coupon(*, batch_id: int, user_id: str) -> Coupon:
    batch = CouponBatch.objects.select_for_update().get(id=batch_id)

    if batch.expires_at <= timezone.now():
        raise ValueError("BATCH_EXPIRED")
    if (
        Coupon.objects.filter(batch=batch, issued_to=user_id).count()
        >= batch.per_user_limit
    ):
        raise ValueError("PER_USER_LIMIT_REACHED")
    if Coupon.objects.filter(batch=batch).count() >= batch.total_limit:
        raise ValueError("BATCH_LIMIT_REACHED")

    # 코드 충돌 대비 재시도
    for _ in range(5):
        code = _gen_code()
        if not Coupon.objects.filter(code=code).exists():
            break
    else:
        raise RuntimeError("CODE_GENERATION_FAILED")

    return Coupon.objects.create(
        batch=batch,
        code=code,
        issued_to=user_id,
        issued_at=timezone.now(),
        status=Coupon.STATUS_ISSUED,
    )


@transaction.atomic
def redeem_coupon(*, code: str, user_id: str, order_id: str) -> Coupon:
    coupon = Coupon.objects.select_for_update().select_related("batch").get(code=code)

    if coupon.batch.expires_at <= timezone.now():
        raise ValueError("COUPON_EXPIRED")
    if coupon.status == Coupon.STATUS_REDEEMED:
        raise ValueError("COUPON_ALREADY_REDEEMED")
    # 본인만 사용 정책이면 주석 해제
    # if coupon.issued_to and coupon.issued_to != user_id:
    #     raise ValueError("COUPON_OWNERSHIP_MISMATCH")

    coupon.status = Coupon.STATUS_REDEEMED
    coupon.redeemed_by = user_id
    coupon.redeemed_at = timezone.now()
    coupon.order_id = order_id
    coupon.save(update_fields=["status", "redeemed_by", "redeemed_at", "order_id"])
    return coupon
