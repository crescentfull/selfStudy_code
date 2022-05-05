'''
type_checker 데코레이터 만들기 (인자 유효성 검사)
digit1, digit2 를 곱한 값을 출력하는 함수 만들기
type_checker 데코레이터로 digit1, digit2 가 정수가 아니면 'only integer support' 출력하고 끝냄
if (type(digit1) != int) or (type(digit2) != int):
'''

# 데코레이터
def type_checker(function):
    def inner_func(digit1, digit2):
        if (type(digit1) != int) or (type(digit2) != int):                       # <--- 유효성 검사의 예
            print('the only int is supported')
            return 
        return function(digit1, digit2)
    return inner_func

# 데코레이터 사용하기 (유효성 검사)
@type_checker
def divide(digit1, digit2):
    return digit1 * digit2

divide(0.1, 1)