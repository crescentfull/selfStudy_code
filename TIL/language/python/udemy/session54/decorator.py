# Python Decorator Function
import time

# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function
# 데코레이터란 단순히 다른 함수를 감싸서 추가기능을 부여하는 것이다.

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2) #시간지연
        #Do something before 함수실행
        function()
        #Do something after 함수실행
    return wrapper_function

@delay_decorator
def say_hello():
    time.sleep(2)
    print("Hello")
    
@delay_decorator
def say_bye():
    print("Bye")
    
def say_greeting():
    print("How are you?")

say_greeting()

decorated_function = delay_decorator(say_greeting)
decorated_function() 