# 값으로 호출, 참조로 호출의 차이점


def func(x):
    print("x = ", x,"address = ", id(x))
    x += "하세요"
    print("x = ",x, "address = ", id(x))

y = 10 #정수형(변경 불가능한 객체)
y = "안녕" #문자열(변경불가 객체)
print("y = ", y, "address = ", id(y))
func(y) # 함수 호출(값)
print("y = ",y,"address = ",id(y))

print("----------------------------------")
def func_list(x):
    print("x = ", x,"address = ", id(x))
    x.append("하세요")
    print("x = ",x, "address = ", id(x))

y = [10,20,30] #정수형(변경 불가능한 객체)
print("y = ", y, "address = ", id(y))
func(y) # 함수 호출(값)
print("y = ",y,"address = ",id(y))
## id 값 같다.