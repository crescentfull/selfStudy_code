# 원의 면적과 원의 둘레를 구하는 프로그램 작성
# PI = 3.141592 전역 상수를 선언하고 상수를 활용하도록 한다.

PI = 3.141592

# 원의 면적을 구하는 함수를 선언 및 구현
# 원의 면적 공식 : PI * 반지름의 제곰
def main():
    radius = float(input("반지름을 입력하시오 : "))
    print("반지름이",radius,"인 원의 면적은 : ", circleArea(radius))
    print("반지름이",radius,"인 원의 둘레는 : ", circleCircumference(radius))
    
def circleArea(radius):
    return PI * radius * radius

print(circleArea(8))

def circleCircumference(radius): #둘레
    return 2 * PI * radius

# radius = float(input("반지름을 입력하시오 : "))
# print("반지름이",radius,"인 원의 면적은 : ", circleArea(radius))
# print("반지름이",radius,"인 원의 둘레는 : ", circleCircumference(radius))

#위의 식도 함수로 만들수 있다.. 당연!

main() # 프로그램 시작을 알리는 함수 호출