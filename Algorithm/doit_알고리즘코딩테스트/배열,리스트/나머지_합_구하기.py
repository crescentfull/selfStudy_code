'''
백준 10986

N개의 수 A1, A2, ... An이 주어졌을때 연속된 부분의 합이 M으로 나누어 떨어지는 구간의 갯수를 구하는 프로그램을 작성하시오.
즉, Ai + .. +Aj(i<=j)의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구하시오.

# 입력1
5 3
1 2 3 1 2

# 출력1
7

'''

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
answer = 0

S[0] = A[0]

for i in range(1, n):
    S[i] - S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder ==0:
        answer += 1
    C[remainder] += 1
    
for i in range(m):
    # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수 더해줌
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2) # / 연산은 float형태로 반환되어 오류, // 사용

print(answer)        