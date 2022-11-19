# data_list = [(90,80),(85,75),(90,100)] 튜플을 원소로하는
# 리스트를 활용하여 학생의 총점과 평균(소수 첫째자리)을 출력하는 프로그램을
# 작성하시오.
# enumerate() 함수 이용
# 출력결과
# 1번 학생의 총점은 170점이고, 평균은 85.0
# 2본
# 3번

data_list = [(90,80),(85,75),(90,100)]

def score(data_li):
    for data, value in enumerate(data_li):
        print(data)
        print(value)
        s = sum(value)
        avr = s/len(value)
        print(f" 합 ; {s}, 평균 : {avr}")
        
def solve(data_list):
    for i, scores in enumerate(data_list):
        sum = 0
        for score in scores:
            sum += score
        print(i, sum, sum/len(scores))
        
score(data_list)
solve(data_list)