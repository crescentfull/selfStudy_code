# 정수를 사용자로부터 입력받아서 제곱한 값을 반환하는 함수를 만들어 보시오
# ex)사용자가 5를 입력하면 출력값은 25가 되어야 한다.

def square(num):
    return print(f"{num}의 제곱근 : ", num*num)

square(5)
square(2)
square(3)
square(4)

num = int(input("정수를 입력하시오 : "))
square(num)