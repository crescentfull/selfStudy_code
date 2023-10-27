# Python Decorator Function

def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function
# 데코레이터란 단순히 다른 함수를 감싸서 추가기능을 부여하는 것이다.