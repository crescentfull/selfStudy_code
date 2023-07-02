# 구간합, 합 배열을 이용하여 시간 복잡도를 더 줄이기 위해 사용하는 특수한 목적의 알고리즘이다.
# 구간 합 알고리즘을 활용하려면 먼저 합 배열을 구해야한다.
#
## 수 N개가 주어졌을 때 i번째 수에서 j번째 수까지의 합을 구하는 프로그램을 작성하시오

import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split()) # suNo(숫자 개수), quizNo(질의 개수)
numbers = list(map(int, input().split())) # 변수에 숫자 데이터 저장
prefix_sum = [0]        # 합 배열 변수 선언
temp = 0        # 변수 선언

# 저장한 숫자 데이터 차례대로 탐색
for i in numbers:
    temp = temp +i              # temp에 현재 숫자데이터 더하기
    prefix_sum.append(temp)      # 합 배열에 temp 값 저장
    
# for 질의 개수 만큼 반복    
for i in range(quizNo):
    s, e = map(int, input().split())        # 질의 범위 받기(s~e)
    print(prefix_sum[e] - prefix_sum[s-1])    # 구간 합 출력