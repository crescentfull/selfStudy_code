'''
백준 17298
'''
n = int(input())
answer = [0] * n
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]: # 오큰수 조건
        answer[myStack.pop()] = A[i] # 정답 리스트에 오큰수 저장
    myStack.append(i)
        
while myStack:
    answer[myStack.pop()] = -1
    
result = ""

for i in range(n):
    result += str(answer[i]) + " "

print(result)