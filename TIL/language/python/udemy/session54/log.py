def logging_decorator():
    def wrapper():
        function()
    return wrapper

def a_function(a, b, c):
    return a*b*c

a_function(input[0],input[1],input[2])