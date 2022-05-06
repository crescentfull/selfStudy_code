# 데코레이터 작성하기
import datetime

def datetime_decorator(func):           # <--- datetime_decorator 는 데코레이터 이름, func 가 이 함수 안에 넣을 함수가 됨
    def wrapper():                      # <--- 호출할 함수를 감싸는 함수
        print ('time ' + str(datetime.datetime.now())) # <--- 함수 앞에서 실행할 내용
        func()                          # <--- 함수  
        print (datetime.datetime.now()) # <--- 함수 뒤에서 실행할 내용
    return wrapper                      # <--- closure 함수로 만든다.

# 데코레이터 적용하기
@datetime_decorator    # @데코레이터
def logger_login_david():
    print ("David login")

logger_login_david()

@datetime_decorator    # @데코레이터
def logger_login_anthony():
    print ("Anthony login")

logger_login_anthony()

@datetime_decorator    # @데코레이터
def logger_login_tina():
    print ("Tina login")

logger_login_tina()

#######################################
# Nested function, Closure function 과 함께 데코레이터를 풀어서 작성
# decorator 함수 정의
def outer_func(function):
    def inner_func():
        print('decoration added')
        function()
    return inner_func

# decorating할 함수
def log_func():
    print('logging')
    
# 본래 함수
log_func()

# log_func 함수에 inner_func 함수의 기능을 추가한 decorated_func 함수
decorated_func = outer_func(log_func)
decorated_func()  # <--- 결과는 데코레이터를 사용할 때와 동일함

# 이것을 찐 데코레이터로 하면!
@outer_func
def log_func():
    print('logging')

log_func()

##################################
# 파라미터가 있는 함수에 데코레이터 적용하기
# 데코레이터
def outer_func(function):
    def inner_func(digit1, digit2):
        if digit2 == 0:                       # <--- 유효성 검사의 예
            print('cannot be divided with zero')
            return
        function(digit1, digit2)
    return inner_func

# 데코레이터 사용하기 (유효성 검사)
@outer_func
def divide(digit1, digit2):
    print (digit1 / digit2)
    
divide(4, 2)
divide(9, 0)

##################################
# 파라미터와 관계없이 모든 함수에 적용 가능한 Decorator 만들기
# - 파라미터는 어떤형태이든 결국((args, **kwargs)로 표현 가능
# - 데코레이터의 내부함수 파라미터를 (args, **kwargs)로 작성하면 어떤 함수이든 데코레이터를 적용 가능하다
# 데코레이터 작성
def general_decorator(function):
    def wrapper(*args, **kwargs):
        print("function is decorated")
        return function(*args, **kwargs)
    return wrapper