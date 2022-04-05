from math import *
#지구에서 가장 가까운 별은 프록시마 켄타우리라는 별이라고 한다.
#프록시마 켄타우리는 지구로부터 40 * 10의 12승 km떨어져 있다고 한다.
#빛의 속도로 이 별에 간다면 시간이 얼마나 걸리는지 계산하는 프로그램을 만들어봐라

# 빛의 속도의 값 저장
light_speed = 300000
distance = 40 * pow(10,12)
#print(distance)
seconds = distance / light_speed
print("걸리는 시간(초) : ", seconds)
light_year = seconds/(60 * 60 * 24 * 365)
print("걸리는 년도 : ", light_year)
print( 10 == 10.0)