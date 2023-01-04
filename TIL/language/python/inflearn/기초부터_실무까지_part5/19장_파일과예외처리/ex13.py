# 예외처리
# 예외처리의 목적은 프로그램의 정상적인 종료로 만들어 주는 것이다.
(x, y) = (2, 0)
try :
    z = x/y
    print("try")
except ZeroDivisionError:
    print("모든 수는 0으로 나눌수가 없습니다")