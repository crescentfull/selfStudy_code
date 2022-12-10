'''
원(circle)을 클래스로 표시해보자, 원은 반지름(radius)를 가지고 있다.
원의 넓이와 둘레를 계산하는 메서드를 정의하라
생성자는 매개변수가 존재하는 생성자를 만들어보자

# 출력결과
원의 반지름 : 10
원의 넓이 : 314.16
원의 둘레 : 62.83
'''
from Circle import *

if __name__ == "__main__":
    circle1 = Circle(10)
    circle1.__str__()
    print("원의 둘레 : ", circle1.circleRound())
    print("원의 넓이 : ", circle1.circleArea())
    
    print("-"*40)
    circle1 = Circle(5)
    circle1.__str__()
    print("원의 둘레 : ", circle1.circleRound())
    print("원의 넓이 : ", circle1.circleArea())
    