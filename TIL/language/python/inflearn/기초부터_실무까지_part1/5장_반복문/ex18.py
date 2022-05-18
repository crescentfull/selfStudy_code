# 중첩 루프를 사용하여 아래와 같은 모양을 출력하시오
# *
# **
# ***
# ****
# *****
#1. 5행을 먼저 만든다
for i in range(5):
    i += 1 #이거 없애고 for j in range(i+1)로도 가능
    for j in range(i):
        print("*",end="")
    print("")

#2. format() 함수 이용
# format 함수도 index를 활용하여 출력이 가능
print("정수값 : {}, string : {}, float : {}".format(10,"안녕하세요",10.1))
print("정수값 : {0}, string : {1}, float : {2}".format(10,"안녕하세요",10.1))
print("정수값 : {2}, string : {0}, float : {1}".format(10,"안녕하세요",10.1)) # 인덱스 지정 가능.

# format()함수는 공간확보 및 0으로 채우는 기능도 제공
# 콜론(:)을 기준으로 우측에 > 혹은 < 를 사용해서 방향을 지정해줄수 있다.
print("숫자 '{:>5d}'".format(300)) # > 오른쪽으로 밀어서 출력
print("숫자 '{:<5d}'".format(300)) # < 왼쪽으로 밀어서 출력
for i in range(5):
    print("{:<5}".format("*"*(i+1)))

print(" ")
# 반대로 출력되게 해보자
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
