from rest_framework import serializers
from .models import CouponBatch, Coupon


class CouponBatchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponBatch
        fields = [
            "id",
            "name",
            "discount_type",
            "amount",
            "percent",
            "per_user_limit",
            "total_limit",
            "expires_at",
        ]

    def validate(self, attrs):
        dt = attrs.get("discount_type")
        if dt == CouponBatch.DISCOUNT_FIXED:
            if attrs.get("amount") is None:
                raise serializers.ValidationError(
                    "amount is required for fixed discount_type"
                )
        elif dt == CouponBatch.DISCOUNT_PERCENT:
            p = attrs.get("percent")
            if p is None or not (1 <= p <= 100):
                raise serializers.ValidationError(
                    "percent must be 1..100 for percent discount_type"
                )
        else:
            raise serializers.ValidationError("invalid discount_type")
        return attrs


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            "id",
            "code",
            "status",
            "issued_to",
            "issued_at",
            "redeemed_by",
            "redeemed_at",
            "order_id",
        ]
