# 입력 받은 정수의 부호 (양수, 음수, 0) 출력하기

n = int(input("정수 입력 : "))

if n>0:
    print('양수')
elif n==0:
    print('0')
else:
    print("음수")

# 3개로 분기하는 조건문
n = int(input("정수를 입력 : "))

if n == 1:
    print("A")
elif n == 2:
    print("B")
else:
    print("c")
    
if n == 1:
    print("A")
elif n == 2:
    print("B")
elif n == 3:
    print("c")

# 두 개의 차이?
# 2번쨰 실행해서 4를 입력하면 아무것도 출력이 되지 않는다. 왜? else: pass 가 숨어있기 때문이다.