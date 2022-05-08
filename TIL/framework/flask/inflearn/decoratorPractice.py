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


'''
HTML 웹페이지 태그를 붙여주는 데코레이터 만들기
해당 데코레이터를 사용해서 안녕하세요 출력

예) @mark_bold - 볼드체로 만들기 태그: <b>내용</b>
    @mark_italic - 이텔릭체로 만들기 태그: <i>내용</i>
'''
def mark_bold(function):
    def wrapper(*args, **kwargs):
        return '<b>'+function(*args, **kwargs)+'</b>'
    return wrapper
def mark_italic(function):
    def wrapper(*args, **kwargs):
        return '<i>'+function(*args, **kwargs)+'</i>'
    return wrapper

@mark_bold
@mark_italic
def test(string):
    return string

print(test("hi"))