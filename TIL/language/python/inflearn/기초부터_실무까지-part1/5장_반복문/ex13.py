# 사용자로부터 임의의 갯수의 성적을 입력받아서 합계와 평균을 계산한 후
# 출력하는 프로그램을 작성하시오. 단, 센티넬은 음수의 값을 사용하시오.

cnt = 0
sum = 0
score = 0
avr = 0.0
#센티넬 (보초값)을 사용자에 제시하는 코드
print("종료하시려면 음수를 입력하세요.(예 : -1) :")
while score >= 0:
    score = int(input(str(cnt+1)+"번째 학생의 성적을 입력하세요. : "))
    # 음수 값인지 구하는 코드
    if score >= 0:
        sum += score #성적의 합계를 구하는 코드
        cnt += 1     #학생의 수를 누적하는 코드
        
#합계와 평균을 계산하고 출력하는 코드
if cnt > 0:
    aver = sum/cnt

# 합계와 평균을 출력하는 코드
print(str(cnt+1)+"학생의 평균은 %0.1f입니다" %avr)