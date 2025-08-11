import pytest
from django.utils import timezone
from rest_framework.test import APIClient
from coupons.models import CouponBatch

pytestmark = pytest.mark.django_db


def _mk_batch(**kwargs):
    defaults = dict(
        name="Welcome 10%",
        discount_type="percent",
        percent=10,
        per_user_limit=1,
        total_limit=1000,
        expires_at=timezone.now() + timezone.timedelta(days=365),
    )
    defaults.update(kwargs)
    return CouponBatch.objects.create(**defaults)


def test_issue_and_redeem_idempotent_flow():
    c = APIClient()
    batch = _mk_batch()

    r1 = c.post(
        "/v1/coupons/issue/",
        {"batch_id": batch.id, "user_id": "u1"},
        format="json",
        HTTP_IDEMPOTENCY_KEY="iss-1",
    )
    assert r1.status_code == 200
    code = r1.data["code"]

    r2 = c.post(
        "/v1/coupons/issue/",
        {"batch_id": batch.id, "user_id": "u1"},
        format="json",
        HTTP_IDEMPOTENCY_KEY="iss-1",
    )
    assert r2.status_code == 200 and r2.data["code"] == code

    r3 = c.post(
        "/v1/coupons/issue/",
        {"batch_id": batch.id, "user_id": "u1"},
        format="json",
        HTTP_IDEMPOTENCY_KEY="iss-2",
    )
    assert (
        r3.status_code == 409 and r3.data["error"]["code"] == "PER_USER_LIMIT_REACHED"
    )

    rr1 = c.post(
        "/v1/coupons/redeem/",
        {"code": code, "order_id": "ord_1", "user_id": "u1"},
        format="json",
        HTTP_IDEMPOTENCY_KEY="red-1",
    )
    assert rr1.status_code == 200 and rr1.data["status"] == "redeemed"

    rr2 = c.post(
        "/v1/coupons/redeem/",
        {"code": code, "order_id": "ord_1", "user_id": "u1"},
        format="json",
        HTTP_IDEMPOTENCY_KEY="red-1",
    )
    assert rr2.status_code == 200 and rr2.data["code"] == code

    rr3 = c.post(
        "/v1/coupons/redeem/",
        {"code": code, "order_id": "ord_1", "user_id": "u1"},
        format="json",
        HTTP_IDEMPOTENCY_KEY="red-2",
    )
    assert (
        rr3.status_code == 409
        and rr3.data["error"]["code"] == "COUPON_ALREADY_REDEEMED"
    )
