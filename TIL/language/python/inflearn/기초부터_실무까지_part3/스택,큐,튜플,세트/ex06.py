# 튜플 대입 연산에 대한 실습
# 튜플 패팅(packing) : 튜플에다가 값을 저장하는 과정
# 튜플 언패킹(unpacking) : 튜플에서 값을 추출하여 변수에 대입하는 과정

# 값을 교환할 때 : 일반적 방법
x = 10
y = 20
temp = 0  # 빈 컵의 역할
print("값 변경 전(x,y) : ", x,y)
temp = x
x = y
y = temp
print("값 변경 후(x,y) : ",x,y)
print("--------------------------")
# 값을 교환할 때 : 튜플 이용하는 방법
(a, b) = 100, 200
print("값 변경 전(a,b) : ",a,b)
(c, d) = (b, a)
print("값 변경 전 (c,d) : ",c,d)

# (x,y,z) = (10,20) # unpack value error
person = ("신은혁", 14, "중학생")
(name, age, student_grade) = person
print(name, age, student_grade)
 