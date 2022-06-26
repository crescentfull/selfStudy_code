# 값에 의한 호출(call by value), 값에 의한 전달(paas by value)은 동일한 개념이다
# 함수를 호출할 때, 값이 복사가 되어진다(중요)
# 호출한 곳에 영향을 끼치지 않는다.
# 숫자 객체는 변경될 수 없는 immutable object이다.

def change(num):
    num = num + 10
    print("change()내의 num의 값 : ",num)
    print("change()내의 num의 주소값 : ",id(num))
    return num   
#파이썬에서는 모든 값들이 객체로 되어있다.
n = 100
print("호출 전 n의 주소값(id) : ", id(n))
print("호출 전 n의 값 : ", n)
x = change(n)
print("호출 후 x의 주소값(id) : ", id(x))
print("호출 후 x의 값 : ", x)
print("호출 후 n의 주소값(id) : ", id(n))
print("호출 후 n의 값 : ", n)