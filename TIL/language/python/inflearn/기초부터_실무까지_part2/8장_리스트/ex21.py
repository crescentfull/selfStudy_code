# 성적 처리 프로그램

## 성적 정보
# score = [
#        [100,100,100],[20,20,20],[30,30,30],[40,40,40],[50,50,50]
#        ]

## 출력
# 번호 국어 영어 수학 총점 평균
# -----------------------
#  1  100 100 100 300  100.00
#  2  20  20  20  60   20.00
#  3  30  30  30  90   30.00
#  4  40  40  40  120  40.00
#  5  50  50  50  150  40.00
# -----------------------
# 총점 240  240  240  720  48.00

score = [
        [100,100,100],[20,20,20],[30,30,30],[40,40,40],[50,50,50]
        ]

# 과목별 총점을 저장할 변수
korSum = 0
engSum = 0
mathSum = 0

# 전체 합계와 평균을 저장하기 위한 변수
totalSum = 0
avg = 0.0

# 출력 상단부
print("번호     국어    영어    수학    총점    평균")
print("---------------------------------------")

for i in range(len(score)):
    sum = 0     # 개인별 총점
    average = 0.0
    
    korSum += score[i][0] #국어
    engSum += score[i][1] #영어
    mathSum += score[i][2] #수학
    
    # 번호
    print("%3d" % (i+1), end="\t")
    
    for j in range(len(score[i])):
        sum +=score[i][j] # 개인별 총점
        print("\b%d" % score[i][j], end="\t")
    
    totalSum += sum #총합
    average = sum/len(score[i]) # 개인별 평균
    avg += average # 전체 평균 합
    print("\b%d\t%.2f" % (sum, average))

avg = avg/len(score) # 전체 평균점수 구하기
print("---------------------------------------")
print("총점\t%d \t%d \t%d \t%d \t%.2f" % (korSum, engSum, mathSum, totalSum, avg))