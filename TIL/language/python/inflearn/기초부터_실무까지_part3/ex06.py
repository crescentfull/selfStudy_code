# 튜플 대입 연산에 대한 실습
# 튜플 패팅(packing) : 튜플에다가 값을 저장하는 과정
# 튜플 언패킹(unpacking) : 튜플에서 값을 추출하여 변수에 대입하는 과정

# 값을 교환할 때 : 일반적 방법
x = 10
y = 20
temp = 0  # 빈 컵의 역할
print("값 변경전(x,y) : ", x,y)
temp = x
x = y
y = temp