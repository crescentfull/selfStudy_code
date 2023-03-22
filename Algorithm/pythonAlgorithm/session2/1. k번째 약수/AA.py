import sys
# sys.stdin=open("in2.txt", "rt")
n,k = map(int, input().split())
print(n,k)
cnt=0
for x in range(1, n+1):
    if n%x == 0:
        cnt += 1
    if cnt == k:
        print(x)
        break
else:
    print(-1)