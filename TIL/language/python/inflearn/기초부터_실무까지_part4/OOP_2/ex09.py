'''
method overriding
상속관계에서 조상클래스의 멤버메서드를 자손클래스에서 상속받아서 자신의 기능에 맞게끔 수정을 한다.
(modify, change) 재정의
단, 메서드의 선언부는 반드시 동일하고 구현부만 다르게하는 것
'''

# 부모클래스 정의
class Car:
    speed = 0
    def upSpeed(self, speed):
        self.speed += speed
        print(f"현재속도(부모클래스) : {self.speed}")
    def __downSpeed(self, speed):
        self.speed -= speed
        print(f"현재속도(부모클래스) : {self.speed}")
    def call(self):
        self.__downSpeed(100)
# 자식클래스 정의
class Sedan(Car):
    # 메서드 오버라이딩
    def upSpeed(self, speed):
        self.speed += speed
        # 150km
        if self.speed > 150:
            self.speed = 150
            print(f"150km를 넘을 수 없습니다.")
        print(f'현재속도(자식클래스) : {self.speed}')
    def downSpeed(self, speed):
        self.speed -= speed
        print(f"현재속도(자식클래스) : {self.speed}")    

# 자식 클래스 truck
class Truck(Car):
    # 구현부 pass -> 부모클래스의 멤버만 상속받고 자신의 멤버는 추가하지 않는다
    pass

if __name__ == '__main__':
    sedan1 = None
    truck1 = None
    
    sedan1 = Sedan()
    truck1 = Truck()
    print("승용차의 속도 : ", end=" ")
    # 메서드 오버라이딩이 되어진 자식클래스의 upSpeed() 메서드가 호출 
    sedan1.upSpeed(2000)
    truck1.upSpeed(2000)
    # __메서드명() 형태에서는 메서드를 호출 불가능
    # sedan1.__downSpeed(100)
    sedan1.downSpeed(100)
    # truck 인스턴스는 __downSpeed를 호출 불가
    car = Car()
    car.call()