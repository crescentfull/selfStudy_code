from django.urls import path
from .views import CouponBatchCreate, CouponIssue, CouponRedeem, CouponList

urlpatterns = [
    path("coupon-batches/", CouponBatchCreate.as_view()),
    path("coupons/issue/", CouponIssue.as_view()),
    path("coupons/redeem/", CouponRedeem.as_view()),
    path("coupons/", CouponList.as_view()),
]
