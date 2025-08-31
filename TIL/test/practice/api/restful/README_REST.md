# RESTful 주문 처리 API

기존 `api_2.py`의 도메인 로직을 RESTful API로 변환한 버전입니다.


### 1. API 문서 확인
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 2. 테스트 실행
```bash
# 서버가 실행 중인 상태에서 다른 터미널에서
python test_api.py
```

## API 엔드포인트

### 주문 관리
- `POST /orders` - 주문 생성
- `GET /orders/{order_id}` - 주문 조회

### 쿠폰 관리  
- `GET /coupons/{coupon_code}` - 쿠폰 조회
- `POST /coupons/{coupon_code}/validate` - 쿠폰 검증

### 유틸리티
- `GET /health` - 헬스체크

## 주요 기능

### 1. 주문 생성 (`POST /orders`)
```bash
curl -X POST "http://localhost:8000/orders" \
     -H "Content-Type: application/json" \
     -H "Idempotency-Key: my-unique-key" \
     -d '{
       "user_id": "user123",
       "items": [
         {"sku": "ITEM001", "qty": 2, "price": 10000}
       ],
       "coupon_code": "DISCOUNT10"
     }'
```

**응답:**
```json
{
  "order_id": "ORD000001",
  "user_id": "user123",
  "items": [
    {"sku": "ITEM001", "qty": 2, "price": 10000}
  ],
  "subtotal": 20000,
  "discount": 2000,
  "total": 18000,
  "coupon_code": "DISCOUNT10",
  "created_at": "2023-12-01T10:30:00Z"
}
```

### 2. 주문 조회 (`GET /orders/{order_id}`)
```bash
curl "http://localhost:8000/orders/ORD000001"
```

### 3. 쿠폰 검증 (`POST /coupons/{coupon_code}/validate`)
```bash
curl -X POST "http://localhost:8000/coupons/DISCOUNT10/validate"
```

## 주요 개선사항

### 1. RESTful 설계
- **리소스 중심**: `/orders`, `/coupons` 등 명사형 URL
- **HTTP 메서드**: GET, POST 적절히 활용
- **상태 코드**: 201(생성), 404(없음), 400(잘못된 요청) 등

### 2. 입력 검증 및 문서화
- **Pydantic 모델**: 자동 검증 및 직렬화
- **OpenAPI 문서**: Swagger UI로 대화형 문서
- **예제 데이터**: 스키마에 예제 포함

### 3. 에러 처리
```json
{
  "error_code": "INVALID_QUANTITY",
  "message": "수량은 1 이상이어야 합니다. 입력값: 0",
  "details": {
    "qty": 0,
    "item_sku": "ITEM001"
  }
}
```

### 4. 멱등성 지원
- `Idempotency-Key` 헤더로 중복 처리 방지
- 동일한 키로 요청 시 캐시된 결과 반환

### 5. 의존성 주입
- FastAPI의 `Depends` 시스템 활용
- 테스트 및 확장성 향상

## 아키텍처

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   API Layer     │    │  Domain Layer   │    │Infrastructure   │
│                 │    │                 │    │     Layer       │
│ • FastAPI       │───▶│ • Use Cases     │───▶│ • Repositories  │
│ • Pydantic      │    │ • Domain Rules  │    │ • Services      │
│ • Error Handler │    │ • Domain Errors │    │ • In-Memory DB  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🧪 테스트 시나리오

`test_api.py`에서 다음을 테스트합니다:

1. **정상 케이스**
   - 주문 생성 및 조회
   - 쿠폰 조회 및 검증

2. **에러 케이스**
   - 잘못된 수량 (qty ≤ 0)
   - 존재하지 않는 주문/쿠폰
   - 유효하지 않은 쿠폰

3. **멱등성**
   - 동일한 키로 중복 요청
   - 캐시된 결과 반환 확인

## 기존 코드와의 차이점

| 구분 | 기존 (`api_2.py`) | RESTful (`api_restful.py`) |
|------|-------------------|----------------------------|
| **인터페이스** | 함수 호출 | HTTP API |
| **데이터 형식** | Python 객체 | JSON |
| **검증** | 수동 검증 | Pydantic 자동 검증 |
| **에러 처리** | Exception | HTTP 상태 코드 + JSON |
| **문서화** | 코멘트 | OpenAPI/Swagger |
| **테스트** | pytest | HTTP 요청 테스트 |

## 다음 단계

실무에서 추가로 고려할 사항들:

1. **인증/인가**: JWT, OAuth2 등
2. **데이터베이스**: PostgreSQL, MongoDB 등  
3. **캐싱**: Redis 등
4. **로깅**: 구조화된 로깅
5. **모니터링**: Prometheus, Grafana 등
6. **배포**: Docker, Kubernetes 등
