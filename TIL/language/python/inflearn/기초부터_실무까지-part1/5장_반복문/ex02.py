# range() 함수 실습하기
# 1.range(x) 매개변수 1개짜리 함수를 이용
sum = 0
for x in range(10):
    sum += x
print("1. 0~9까지의 누계합 : ", sum)
print("---------------------------------")
#2. range(start,stop) 매개변수 2개짜리 함수를 이용
# 누적을 하는데 stop 값은 포함하지 않는다.
sum = 0
for x in range(0,10):
    sum = sum + x
print("2. 0~9까지의 누계합 : ", sum)
print("---------------------------------")
#3. range(start,stop,step) 매개변수 3개짜리 함수를 이용
# 누적을 하는데 stop 값은 포함하지 않는다. 
# step만큼 건너띄어 리스트를 생성
sum = 0
for x in range(0,10,2):
    sum = sum + x
print("3. 0~9까지의 누계합 : ", sum)
print("---------------------------------")

#문자열 실습 
# 문자열도 시퀀스의 대상에 포함된다. for 문을 통해 문자를 추출하여 출력할 수가 있다.
s = "shin eun hyeok"
for char in s:
    print(char)