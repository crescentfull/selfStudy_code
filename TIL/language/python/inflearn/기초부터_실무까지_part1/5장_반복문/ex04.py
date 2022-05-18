# 1~100까지의 누적 합계를 구하시오. 단, 합계가 2000이상이 되면 멈추는 프로그램을 작성하시오

sum = 0

for i in range(101):
    if sum >= 2000:
        print("2000이상입니다. 종료합니다")
        print("마지막 i : ",i)
        print("합계 : ",sum)
        break
    else:
        sum += i