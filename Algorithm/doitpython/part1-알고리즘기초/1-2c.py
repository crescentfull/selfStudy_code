# 세정수를 입력받아 중앙값 구하기

def med3(a,b,c):
    if a>=b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b
    
print("세 정수의 중앙값을 구합니다.")
a = int(input('정수 a 값 : '))
b = int(input('정수 b 값 : '))
c = int(input('정수 c 값 : '))

print(f"중앙 값은 {med3(a,b,c)}입니다.")

def otherWay(a,b,c):
    if ( b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b ) or (a < b and c > b):
        return b
    return c

print(f"중앙 값은 {otherWay(a,b,c)}입니다.")

"""
med3() 보다 otherWay()의 효율을 좋지 않다...!
a와 b의 비교를 이미 마친상태에서 또한번 하는 것은 효율적이지 못하기 때문이다.
"""