'''
인스턴스 변수 : 인스턴스를 생성해야 비로소 사용할 수 있는 변수
인스턴스 변수는 메모리 공간에 독립적으로 공간을 차지하고 있어서 해당 인스턴스에게만 영향을 끼친다
인스턴스 변수는 접근 방법 : 인스턴스명.인스턴스 변수명

클래스 변수 : 클래스가 로딩이 되면서 메모리 상당(메소드 영역, 클래스 영역)
미리 공간을 할당하고 저장된다. 클래스 변수는 모든 인스턴스에게 공유되는 변수를 클래스 변수라고 한다.
클래스 변수의 접근 방법 : 클래스명.클래스 변수명(권장사항)
클래스 변수 값의 변경은 모든 인스턴스에 영향을 끼친다.
'''
# 클래스 변수는 인스턴스 생성 없이도 접근이 가능

class Car:
    # car 클래스 필드
    color = ""  # 인스턴스 변수
    speed = 0   # 인스턴스 변수
    count = 0   # 클래스 변수는 반드시 필드로 선언해줘야한다.
    
    # 기본 생성자
    def __init__(self):
        self.color = "노랑"
        self.speed = 0
        Car.count += 1
    
    def __str__(self):
        print(f"color : {self.color}")
        print(f"speed : {self.speed}")
        
        # 아래는 클래스 변수에 접근하는 방법 2가지이다
        # 객체지향 개념에서는 클래스명.클래스변수명 으로 접근하는 것이 올바른 방법
        
        print(f"Car.count : {Car.count}")
        #print(f"self.count : {self.count}")

if __name__ == "__main__":
    #print(Car.count) # 인스턴스를 생성하지 않았는데 값이 출력이 되고 있다.
    print(id(Car.count))
    # 인스턴스 생성
    car1 = Car()
    car1.__str__()
    
    # 파이썬에서는 인스턴스를 생성하면 메모리의 값이 새로이 할당됨을 알 수 있다.
    print(id(Car.count))
    print(id(Car.count))
    car2 = Car()
    car2.__str__()
    print(id(Car.count))
    print(id(Car.count))
    