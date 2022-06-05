# 구의 부피를 구하는 함수 sphereVolume() 작성
# 사용자로부터 반지름 입력받고 구의 부피를 구하라
import fractions,math
def sphereVolume():
    r = int(input("반지름을 입력 : "))
    v = fractions.Fraction(4,3) * math.pi * math.pow(r,3)
    return print("구의 부피는 : ", round(v,2))

sphereVolume()