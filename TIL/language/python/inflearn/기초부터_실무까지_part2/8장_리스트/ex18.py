# 2차원 리스트는 메모리에 연속적으로 들어가있다.
# 파이썬에서 리스트는 2차원 가능 = 행렬

# 2차원 list 동적 생성
rows = 3
cols = 5
s = []

for row in range(rows):
    s += [[0]*cols]
print("s = ", s)

r = [([0]* cols) for now in range(rows)] # list comprehension
print(r)