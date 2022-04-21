# 임의의 숫자를 발생시켜 숫자를 맞추는 게임을 만들어 보기

from random import *

cnt = 0
num = randint(1,100)
print("발생ㅎ안 난수의 값 : ",num)

print("1부터 100사이의 숫자를 맞추어 보세요")
print("기회는 단 10번입니다.")

while cnt < 10:
    guess = int(input("숫자를 입력하세요 (1~100): "))
    cnt += 1
    
    if guess < num:
        print("입력한 수가 난수보다 낮습니다.")
    elif guess > num:
        print("입력한 수가 난수보다 높습니다.")
    elif guess == num:
        print("정답입니다. 시도횟수 : ",cnt)
        code = input("게임 종료? (y/n) : ")
        # 중첩 if 문이 들어가서 게임의 지속 여부를 확인하는 코드
        if code == "n": # 게임 종료 코드
            print("게임을 종료합니다.")
            break
        else:
            print("**************************")
            print("게임을 재시작합니다.")
            #게임을 재시작 하기위해 다시 난수발생과 cnt를 초기화 해야한다.
            num = randint(1,100)
            print("발생ㅎ안 난수의 값 : ",num)
            cnt = 0
print("10회가 넘었습니다.")