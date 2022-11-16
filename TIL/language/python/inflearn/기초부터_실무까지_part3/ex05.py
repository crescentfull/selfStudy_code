# 튜플(tuple)

# 튜플의 특징 : 리스트에 반하여 변경이 불가능한 객체, 리스트에 비해서 속도가 빠름
# 시퀀스의 일종이다.
# +, *, min(), max(), len(), tuple() 연산과 내장함수 사용가능
# 리스트 => [] // 튜플 => ()

colors = ("red", "blue", "yellow")
print(colors)
print(type(colors))

numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))

tuple1 =(1,2,3,11.2,"d","s")
print(tuple1)

# 공백 튜플 
tuple2 = ()
# 튜플은 한번 생성되어지면 더이상 추가,삭제, 수정이 불가함
# tuple2[0] = 100 >>> error
print(tuple2)

tuple3 = (10)
print(tuple3)

li = [1,2,3,4,5]
print(li)
tuple4 = tuple(li)
print(tuple4)

print("****************************************")
# 튜플도 리스트와 마찬가지로 내장 튜플을 가질 수 있다.
t1 = (1, 2.2, "반가워요")
t2 = t1, (3.3, 4.4, 5.5)
t3 = t1,t2

print(t1)
print(t2)
print(t3)
print(type(t2))
print("t1 주소 : ", id(t1))
print("t2 주소 : ", id(t2))
print("t3 주소 : ", id(t3))
print("t2[0]의 주소 : ", id(t2[0]))
print("t2[1]의 주소 : ", id(t2[1]))
print("t3[0]의 주소 : ", id(t3[0]))
print("t3[1]의 주소 : ", id(t3[1]))
print("t3[1][0]의 주소 : ", id(t3[1][0]))
print(t3[1][0])

# print("t3[2]의 주소 : ", id(t3[2]))
print("****************************************")

print(dir(t1)) # 사용가능한 함수 체크

print("****************************************")
# 튜플 비교 함수
print(t1.__eq__(t2))