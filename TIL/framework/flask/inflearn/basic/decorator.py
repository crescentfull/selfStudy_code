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
print ("*******************************")
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
print ("*******************************")
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
print ("*******************************")
# 파라미터와 관계없이 모든 함수에 적용 가능한 Decorator 만들기
# - 파라미터는 어떤형태이든 결국((args, **kwargs)로 표현 가능
# - 데코레이터의 내부함수 파라미터를 (args, **kwargs)로 작성하면 어떤 함수이든 데코레이터를 적용 가능하다
# 데코레이터 작성 
def general_decorator(function):
    def wrapper(*args, **kwargs):
        print("function is decorated")
        return function(*args, **kwargs)
    return wrapper

# 데코레이터 적용하기
@general_decorator
def calc_square(digit):
    return digit * digit

@general_decorator
def calc_plus(digit1, digit2):
    return digit1 + digit2

@general_decorator
def calc_quad(digit1, digit2, digit3, digit4):
    return digit1 * digit2 * digit3 * digit4

# 함수 호출하기
print (calc_square(2))
print (calc_plus(2, 3))
print (calc_quad(2, 3, 4, 5))

##################################
print ("*******************************")
# 한 함수에 데코레이터 여러 개 지정하기
# 함수에 여러 개의 데코레이터 지정 가능 (여러 줄로 @데코레이터를 써주면 됨)
# 데코레이터를 나열한 순서대로 실행됨
# 여러 데코레이터 작성하기
def decorator1(function):
    def wrapper():
        print('decorator1')
        function()
    return wrapper
 
def decorator2(function):
    def wrapper():
        print('decorator2')
        function()
    return wrapper

# 여러 데코레이터를 함수에 한번에 적용하기
@decorator1
@decorator2
def hello():
    print('hello')

hello()

################################
print ("*******************************")
# method decorator
# 클래스의 메드 데코레이터 적용가능
# 클래스 method는 첫 파라미터가 self 이므로 이부분을 데코레이터에 작성시에 포함시켜야 함
# decorator 작성하기(for method)
def h1_tag(function):
    def func_wrapper(self,*args, **kwargs):# <--- self 를 무조건 첫 파라미터로 넣어야 메서드에 적용가능
        return "<h1>{0}</h1>".format(function(self,*args,**kwargs))# <--- function 함수에도 self 를 넣어야 함
    return func_wrapper

#클래스 선언시에 메서드 데코레이터 적용하기
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    @h1_tag
    def get_name(self):
        return self.first_name + ' ' + self.last_name

#데코레이터 적용 확인해보기
davelee = Person('lee','dave')
print(davelee.get_name())

#파이썬 format 함수 이해하기
print('{},{},{}'.format(10,100,1000))
print('{0},{0},{2}'.format(10,100,1000))
print('{2},{1},{1}'.format(10,100,1000))

##################################
print ("*******************************")
#파라미터가 있는 데코레이터 만들기 (심화)
#decorator에 파라미터 추가 가능
def decorator1(num):
    def outer_wrapper(function):
        def inner_wrapper(*args,**kwargs):
            print('deocrator1 {}'.format(num))
            return function(*args,**kwargs)
        return inner_wrapper
    return outer_wrapper

def print_hello():
    print('hello')
    
print_hello1 = decorator1(1)(print_hello)
print_hello1()
### decorator로 바꿔보자
@decorator1(4)
def print_hello():
    print('hello')            

print_hello()