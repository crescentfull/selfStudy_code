# 내장함수 및 math 라이브러리 함수 이용
from math import * #from은 라이브러리가져오는거 math라이브러리의 모든 함수를 사용할수 있게끔 한다.

#절댓값
print(abs(-77))
#반올림
print(round(1.222))
print(round(1.5222))
#최댓값(매개변수 값 중에서)
print(max(10, - 20, 100, 9999))
#최솟값
print(min(10, - 20, 100, 9999))
#제곱근
print(sqrt(4.0))
#3의 제곱 구하기, 연산자 **와 동일한 것
print(pow(3, 2))