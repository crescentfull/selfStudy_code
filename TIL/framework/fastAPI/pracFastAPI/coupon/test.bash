# 1) 쿠폰 등록 (고유 code 생성 또는 직접 지정 가능)
curl -X POST http://127.0.0.1:8000/v1/coupons \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: reg-001" \
  -d '{"code": "WELCOME10", "discount_type": "percent", "amount": 10, "expires_at": null}'

# 2) 목록 조회
curl "http://127.0.0.1:8000/v1/coupons?only_active=true&limit=20&offset=0"

# 3) 단건 조회
curl http://127.0.0.1:8000/v1/coupons/WELCOME10

# 4) 쿠폰 사용(등록코드 입력) - 사용자 u1가 사용
curl -X POST http://127.0.0.1:8000/v1/coupons/redeem \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: red-001" \
  -d '{"code":"WELCOME10","user_id":"u1"}'

# 5) 같은 Idempotency-Key로 다시 호출하면 같은 응답 재생(중복 사용 방지)
curl -X POST http://127.0.0.1:8000/v1/coupons/redeem \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: red-001" \
  -d '{"code":"WELCOME10","user_id":"u1"}'
