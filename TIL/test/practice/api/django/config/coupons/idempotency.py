# coupons/idempotency.py
import hashlib, json
from functools import wraps
from django.db import transaction
from rest_framework.response import Response
from .models import IdempotencyKey


def _fingerprint(path: str, body: dict) -> str:
    data = json.dumps(
        {"path": path, "body": body}, sort_keys=True, separators=(",", ":")
    ).encode()
    return hashlib.sha256(data).hexdigest()


def _get_idempotency_key(request) -> str | None:
    req = getattr(request, "_request", request)
    return (
        getattr(request, "headers", {}).get("Idempotency-Key")
        or getattr(req, "META", {}).get("HTTP_IDEMPOTENCY_KEY")
        or getattr(req, "META", {}).get("Idempotency-Key")
        or getattr(req, "META", {}).get("HTTP_IDEMPOTENCYKEY")
    )


def idempotent_view(view_func):
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        key = _get_idempotency_key(request)
        if not key:
            return Response(
                {
                    "error": {
                        "code": "IDEMPOTENCY_KEY_REQUIRED",
                        "message": "Provide Idempotency-Key",
                    }
                },
                status=400,
            )

        body = getattr(request, "data", {}) or {}
        fp = _fingerprint(request.path, body)

        # 선점/재사용: 트랜잭션에서 get_or_create 사용
        with transaction.atomic():
            obj, created = IdempotencyKey.objects.get_or_create(
                key=key,
                defaults={
                    "user_id": str(getattr(request.user, "id", "anon")),
                    "request_fingerprint": fp,
                },
            )
            if not created:
                if obj.request_fingerprint and obj.request_fingerprint != fp:
                    return Response(
                        {
                            "error": {
                                "code": "IDEMPOTENCY_KEY_BODY_MISMATCH",
                                "message": "Idempotency-Key reused with different body",
                            }
                        },
                        status=409,
                    )
                if obj.response_status is not None:
                    # ✅ 항상 DRF Response로 반환
                    return Response(obj.response_body or {}, status=obj.response_status)
                # (희귀) 선행 요청 처리 중
                return Response(
                    {
                        "error": {
                            "code": "REQUEST_IN_PROGRESS",
                            "message": "Try again shortly.",
                        }
                    },
                    status=409,
                )

        # 최초 처리
        response = view_func(self, request, *args, **kwargs)

        # 응답 저장 (분리된 트랜잭션)
        with transaction.atomic():
            IdempotencyKey.objects.filter(key=key).update(
                response_status=response.status_code,
                response_body=(getattr(response, "data", None) or {}),
            )

        return response

    return wrapper
