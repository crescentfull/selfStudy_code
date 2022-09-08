from webbrowser import get
from calc import *

num1,num2 = map(int, input("숫자를 입력하시오 : ").split(","))
print(type(num1))
print(num2)
bigger(num1,num2)
get_max(num1,num2)
get_min(num1, num2)
square(num1)
power(num1,num2)