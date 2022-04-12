# 숫자 추측 게임 만들기
from random import *
# 1~100까지 임의의 수(난수)를 발생시키는 코드
rand_num = randint(1,100)

print("숫자를 맞춰보세요.(1~100")
print("랜덤값 : ",rand_num)
user_num = int(input("숫자를 맞춰보세요 (1~100) : "))
cnt = 0;
while True:
    if user_num == rand_num:
        print(f"정답입니다. 게임을 종료합니다.(시도횟수 : {cnt})")
        break
    elif user_num > rand_num:
        print("입력한 숫자가 큽니다.")
        cnt += 1 #파이썬에서는 ++,-- 이런 증감연산자는 없다. 복합대입연산자를 사용
        print("시도횟수 : ",cnt)
    else:
        print("입력한 숫자가 작습니다.")
        cnt += 1
        print("시도횟수 : ",cnt)
    user_num = int(input("다시입력해주세요 : "))