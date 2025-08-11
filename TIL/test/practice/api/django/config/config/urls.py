from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include("coupons.urls")),  # ← coupons 앱의 라우트
]
