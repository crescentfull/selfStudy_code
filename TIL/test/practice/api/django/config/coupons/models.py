from django.db import models
from django.utils import timezone
from datetime import timedelta


def idempotency_default_expiry():
    return timezone.now() + timedelta(hours=24)


class CouponBatch(models.Model):
    DISCOUNT_FIXED = "fixed"
    DISCOUNT_PERCENT = "percent"
    DISCOUNT_CHOICES = [(DISCOUNT_FIXED, "fixed"), (DISCOUNT_PERCENT, "percent")]

    name = models.CharField(max_length=80)
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_CHOICES)
    amount = models.IntegerField(null=True, blank=True)  # fixed일 때 사용
    percent = models.IntegerField(null=True, blank=True)  # percent일 때 1..100
    per_user_limit = models.IntegerField(default=1)
    total_limit = models.IntegerField()
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.discount_type})"


class Coupon(models.Model):
    STATUS_ISSUED = "issued"
    STATUS_REDEEMED = "redeemed"
    STATUS_CANCELLED = "cancelled"
    STATUS_EXPIRED = "expired"
    STATUS_CHOICES = [
        (STATUS_ISSUED, "issued"),
        (STATUS_REDEEMED, "redeemed"),
        (STATUS_CANCELLED, "cancelled"),
        (STATUS_EXPIRED, "expired"),
    ]

    batch = models.ForeignKey(
        CouponBatch, on_delete=models.PROTECT, related_name="coupons"
    )
    code = models.CharField(max_length=16, unique=True)
    issued_to = models.CharField(max_length=64, null=True, blank=True)
    issued_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_ISSUED
    )
    redeemed_by = models.CharField(max_length=64, null=True, blank=True)
    redeemed_at = models.DateTimeField(null=True, blank=True)
    order_id = models.CharField(max_length=64, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} [{self.status}]"


class IdempotencyKey(models.Model):
    key = models.CharField(max_length=64, unique=True)
    user_id = models.CharField(max_length=64)
    request_fingerprint = models.CharField(max_length=128, null=True, blank=True)
    response_status = models.IntegerField(null=True, blank=True)
    response_body = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=idempotency_default_expiry)
