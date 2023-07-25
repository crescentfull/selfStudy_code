'''
백준 11003번
'''

# 1. 최솟값 가능성이 없는 데이터 삭제
# 2. window 크기 밖 데이터 삭제

'''
N(데이터 개수) L(최솟값을 구하는 범위)
myDeque(데이터를 담을 덱 자료구조)
now(주어진 숫자 데이터를 가지는 리스트)

for N만큼 반복: # now 리스트를 탐색(now[i]를 현재 값으로 세팅
    덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거 1.
    덱의 마지막 위치에 현재 값 저장
    덱의 1번째 위치에서부터 L의 범위를 벗어난 값(now index-L <= index)을 덱에서 제거 2.
    덱의 1번째 데이터 출력
'''

import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
myDeque = deque() # 시간 복잡도를 줄이기 위해서 사용
now = list(map(int, input().split()))

for i in range(N):
    while myDeque and myDeque[-1][0] > now[i]:
        myDeque.pop()
    myDeque.append((now[i], i))
    if myDeque[0][1] <= i-L : # 윈도우 범위를 벗어나면
        myDeque.popleft()
    print(myDeque[0][0], end='  ')
        