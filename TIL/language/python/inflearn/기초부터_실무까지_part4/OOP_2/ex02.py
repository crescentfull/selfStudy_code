'''
특수메소드 : 인스턴스간에 산술연산과 비교연산을 해주는 메서드
예) 인스턴스 a, b가 존재한다면 a+b를 하게 된다면 주소 + 주소가 되는 형태이기 때문에 연산이 불가
+ 연산이 가능하게 하려면 __add()__클래스 안에 메서드로 정의를 해주면 된다.

'''
class Circle:
    def __init__(self, radius=0):
        print("생성자")
        self.radius = radius
    # 2개의 인스턴스를 매개변수로 받는다.(주소값 공유)
    def __eq__(self, other): # 연산자 역할
        print("__eq__")
        return self.radius == other.radius

if __name__ == "__main__":
    circle1 = Circle(10)
    circle2 = Circle(10)
    # 주소값끼리의 연산은 불가능하다. 
    # 인스턴스간의 == 연산자는 __eq()__ 메서드를 호출한 것
    if circle1 == circle2:
        print("원의 반지름이 동일합니다.")