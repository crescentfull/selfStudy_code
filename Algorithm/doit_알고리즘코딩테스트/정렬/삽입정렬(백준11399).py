N = int(input())
A = list(map(int, input().split()))
S = [0]*N

# 삽입정렬

for i in range(1, N):
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0
            
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value
    
S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]
    