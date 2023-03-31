'''
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열 중에서 s번째부터 e번째까지의 수를
오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
'''

import sys
sys.stdin=open("input.txt","rt")

n,k = map(int, input().split())
a = list(map(int, input().split()))
print(n, k)
print(a)
a.sort()
print(a)
print(a[k-1])