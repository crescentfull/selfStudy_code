# Python Decorator Function
import time

# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function
# 데코레이터란 단순히 다른 함수를 감싸서 추가기능을 부여하는 것이다.

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        #Do something after
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