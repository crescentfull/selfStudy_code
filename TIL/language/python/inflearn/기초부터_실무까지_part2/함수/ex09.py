# 키워드 인수(keyword argument)
# 매개변수에 인수 값을 특정해 준다.

def cal(x,y,z):
    return x-y+z

print(cal(10,100,1000)) # 기본
print(cal(z=10,x=100,y=1000)) # 키워드 인수

#! 장점 : 매개변수의 위치에 상관없이 직접 키워드 값을 할당함으로써 함수를 호출할수 있다.