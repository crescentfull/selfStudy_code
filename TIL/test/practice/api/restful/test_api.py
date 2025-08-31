"""
RESTful API 테스트 예제
"""

import requests
import json

# API 서버 주소
BASE_URL = "http://localhost:8000"


def test_create_order():
    """주문 생성 테스트"""
    print("=== 주문 생성 테스트 ===")

    # 주문 데이터
    order_data = {
        "user_id": "user123",
        "items": [
            {"sku": "ITEM001", "qty": 2, "price": 10000},
            {"sku": "ITEM002", "qty": 1, "price": 5000},
        ],
        "coupon_code": "DISCOUNT10",
    }

    # 멱등성 키 설정
    headers = {"Idempotency-Key": "test-order-001"}

    # POST 요청
    response = requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)

    print(f"상태 코드: {response.status_code}")
    print(f"응답: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")

    if response.status_code == 201:
        return response.json()["order_id"]
    return None


def test_get_order(order_id):
    """주문 조회 테스트"""
    print(f"\n=== 주문 조회 테스트 (ID: {order_id}) ===")

    response = requests.get(f"{BASE_URL}/orders/{order_id}")

    print(f"상태 코드: {response.status_code}")
    print(f"응답: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")


def test_get_coupon():
    """쿠폰 조회 테스트"""
    print("\n=== 쿠폰 조회 테스트 ===")

    response = requests.get(f"{BASE_URL}/coupons/DISCOUNT10")

    print(f"상태 코드: {response.status_code}")
    print(f"응답: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")


def test_validate_coupon():
    """쿠폰 검증 테스트"""
    print("\n=== 쿠폰 검증 테스트 ===")

    response = requests.post(f"{BASE_URL}/coupons/DISCOUNT20/validate")

    print(f"상태 코드: {response.status_code}")
    print(f"응답: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")


def test_error_cases():
    """에러 케이스 테스트"""
    print("\n=== 에러 케이스 테스트 ===")

    # 잘못된 수량
    print("1. 잘못된 수량:")
    bad_order = {
        "user_id": "user123",
        "items": [{"sku": "ITEM001", "qty": 0, "price": 10000}],
    }
    response = requests.post(f"{BASE_URL}/orders", json=bad_order)
    print(f"상태 코드: {response.status_code}")
    print(f"응답: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")

    # 존재하지 않는 주문 조회
    print("\n2. 존재하지 않는 주문:")
    response = requests.get(f"{BASE_URL}/orders/NONEXISTENT")
    print(f"상태 코드: {response.status_code}")
    print(f"응답: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")

    # 잘못된 쿠폰
    print("\n3. 잘못된 쿠폰:")
    bad_coupon_order = {
        "user_id": "user123",
        "items": [{"sku": "ITEM001", "qty": 1, "price": 10000}],
        "coupon_code": "INVALID_COUPON",
    }
    response = requests.post(f"{BASE_URL}/orders", json=bad_coupon_order)
    print(f"상태 코드: {response.status_code}")
    print(f"응답: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")


def test_idempotency():
    """멱등성 테스트"""
    print("\n=== 멱등성 테스트 ===")

    order_data = {
        "user_id": "user456",
        "items": [{"sku": "ITEM003", "qty": 1, "price": 15000}],
    }

    headers = {"Idempotency-Key": "idempotent-test-001"}

    # 첫 번째 요청
    print("첫 번째 요청:")
    response1 = requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)
    print(f"상태 코드: {response1.status_code}")
    result1 = response1.json()
    print(f"주문 ID: {result1.get('order_id')}")

    # 두 번째 요청 (동일한 멱등성 키)
    print("\n두 번째 요청 (동일한 멱등성 키):")
    response2 = requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)
    print(f"상태 코드: {response2.status_code}")
    result2 = response2.json()
    print(f"주문 ID: {result2.get('order_id')}")

    print(f"\n동일한 주문 ID인가? {result1.get('order_id') == result2.get('order_id')}")


if __name__ == "__main__":
    print("RESTful API 테스트 시작")
    print("서버가 실행 중인지 확인하세요: python api_restful.py")
    print("-" * 50)

    try:
        # 헬스체크
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ 서버가 정상적으로 실행 중입니다")
        else:
            print("❌ 서버 연결 실패")
            exit(1)
    except requests.exceptions.ConnectionError:
        print("❌ 서버에 연결할 수 없습니다. 서버를 먼저 실행하세요.")
        exit(1)

    # 테스트 실행
    order_id = test_create_order()

    if order_id:
        test_get_order(order_id)

    test_get_coupon()
    test_validate_coupon()
    test_error_cases()
    test_idempotency()

    print("\n" + "=" * 50)
    print("모든 테스트 완료!")
