#파이썬에서 자형 (Data-type)
from math import *
#int형
print(type(17))
#float
print(type(10.223))
#str
print(type("ㅇㅇㅇㅇ"))

#반지름이 r인 구의 부피는 4/3(3분의4 , 분자/분모) * PI * r 
#반지름 5인 구의 부피를 계산하는 프로그램

#문자열 + float은 타입이 일치가 안되어서 문자열을 생성할 수 없다
#해결하기 위한 방안은

r = 5.0
# volume = 4.0/3.0 * pi * r**3
volume = 4.0/3.0 * pi * pow(r,3)
print("구의 부피 : ", volume)
print(pi)

#구의 겉넓이 공식 : 4 * pi * r의 제곱
outer_area = 4 * pi * pow(r,2)
print("구의 겉넓이 : " , outer_area)