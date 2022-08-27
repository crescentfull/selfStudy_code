# 원의 면적과 원의 둘레를 구하는 프로그램 작성
# PI = 3.141592 전역 상수를 선언하고 상수를 활용하도록 한다.

PI = 3.141592

# 원의 면적을 구하는 함수를 선언 및 구현
# 원의 면적 공식 : PI * 반지름의 제곰

def circleArea(radius):
    return PI * radius * radius

print(circleArea(8))

def circleCircumference(radius):
    return 2 * PI * radius