'''
k 번재 큰수

현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 합니다.
기록한 값 중 K번째로 큰 수를 출력하는 프로그램을 작성하세요.
만약 큰 수 부터 만들어진 수가 25 25 23 23 22 20 19 ....이고 K값이 3이라면 k번째 큰 값은 22입니다. 
'''

import sys
sys.stdin = open("input.txt", "rt")
n,k = map(int, input().split())
a = list(map(int, input().split()))

res = set() # 반복 수 없애주기위해서, 중복제거

print(n)
print(k)
print(a)

# 확인용 리스트
# list1 = []
# list2 = []
# list3 = []
# n 만큼 돌려준다
for i in range(n):
    # list1.append(a[i]) 확인
    for j in range(i+1,n):
        # list2.append(a[j]) 확인
        for m in range(j+1, n):
            # print(i, j, m)
            # 각 카드를 합한 값을 res에 넣어준다.
            # list3.append(a[m]) 확인
            res.add(a[i]+a[j]+a[m])
# set은 sort() 적용이 안되니까 list변환            
res = list(res)
res.sort(reverse=True)
# print("list1 :" ,list1)
# print("list2 :" ,list2)
# print("list3 :" ,list3)
print("res :" ,res)
print("K번째 큰수 : " ,res[k-1])