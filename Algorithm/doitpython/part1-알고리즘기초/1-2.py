# 세 정수의 최댓값 구하기

def max3(a, b, c):
    max = a
    if b > max: max = b
    if c > max: max = c
    return max

print(f"max(3,2,1) : {max(3,2,1)}")
print(f"max(10,3,5) : {max(10,3,5)}")
print(f"max(2,9,3) : {max(2,9,3)}")
print(f"max(6,9,7) : {max(6,9,7)}")

""" good """