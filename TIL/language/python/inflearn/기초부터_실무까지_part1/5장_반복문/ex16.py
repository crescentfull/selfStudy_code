# 플래그 변수를 사용한 무한루프 문제
# 1. 증가 / 2. 감속/ 3. 중지를 출력하고 사용자에게 입력 받는 코드
# 증가 => 속도 10씩 증가 
# 감소 => 속도 10씩 감소
# 중지 플래그 변수를 이용하여 무한 루프를 빠져나간다
from traceback import print_tb


run = True#flag변수
#print(type(run))

speed = 0
keyCode = 0

while run:
    print("-----------------------")
    print("1.증가 / 2.감소 / 3.중지(종료)")
    print("-----------------------")
    keyCode = int(input("선택 : "))
    
    #증가
    if keyCode == 1:
        speed += 10
        print("현재속도 : ",speed)
    elif keyCode == 2:
        speed -= 10
        if speed < 0:
            print("현재속도 : ", speed)
            ans = input("음수입니다. 다시 돌아가겠습니까?(y/n) :  ")
            if ans == "y":
                speed = 0
                continue
            elif ans == "n":
                continue
            else:
                print("잘못 입력하였습니다. 다시선택해주세요")
        else:
            print("현재속도 : ",speed)
    elif keyCode == 3:
        run = False #flag변수를 false로 설정해서 루프에서 빠져나오도록
    else:
        print("잘못입력하였습니다.")
print("최종 속도 : ", speed)
print("프로그램 종료!")