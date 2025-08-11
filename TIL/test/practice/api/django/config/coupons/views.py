from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .serializers import CouponBatchCreateSerializer, CouponSerializer
from .models import Coupon, CouponBatch
from .services import issue_coupon, redeem_coupon
from .idempotency import idempotent_view


class CouponBatchCreate(APIView):
    @idempotent_view
    def post(self, request):
        ser = CouponBatchCreateSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        batch = ser.save()
        return Response(
            CouponBatchCreateSerializer(batch).data, status=status.HTTP_201_CREATED
        )


class CouponIssue(APIView):
    @idempotent_view
    def post(self, request):
        batch_id = request.data.get("batch_id")
        user_id = request.data.get("user_id")
        if not batch_id or not user_id:
            return Response(
                {
                    "error": {
                        "code": "VALIDATION",
                        "message": "batch_id and user_id are required",
                    }
                },
                status=400,
            )
        try:
            coupon = issue_coupon(batch_id=batch_id, user_id=user_id)
        except CouponBatch.DoesNotExist:
            return Response({"error": {"code": "BATCH_NOT_FOUND"}}, status=404)
        except ValueError as e:
            return Response({"error": {"code": str(e)}}, status=409)
        return Response(CouponSerializer(coupon).data, status=200)


class CouponRedeem(APIView):
    @idempotent_view
    def post(self, request):
        code = request.data.get("code")
        order_id = request.data.get("order_id")
        user_id = request.data.get("user_id")
        if not code or not order_id or not user_id:
            return Response(
                {
                    "error": {
                        "code": "VALIDATION",
                        "message": "code, order_id, user_id are required",
                    }
                },
                status=400,
            )
        try:
            coupon = redeem_coupon(code=code, user_id=user_id, order_id=order_id)
        except Coupon.DoesNotExist:
            return Response({"error": {"code": "COUPON_NOT_FOUND"}}, status=404)
        except ValueError as e:
            return Response({"error": {"code": str(e)}}, status=409)
        return Response(CouponSerializer(coupon).data, status=200)


class CouponList(APIView):
    def get(self, request):
        user_id = request.GET.get("user_id")
        status_q = request.GET.get("status")
        qs = Coupon.objects.all().order_by("-created_at")
        if user_id:
            qs = qs.filter(Q(issued_to=user_id) | Q(redeemed_by=user_id))
        if status_q:
            qs = qs.filter(status=status_q)
        return Response({"items": CouponSerializer(qs[:50], many=True).data})
