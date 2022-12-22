# super() 메서드 : 자식클래스에서 메서드 오버라이딩을 할 때, 부모클래스의 메서드나 필드를 사용해야 되는 경우가 있다. 이럴때 사용하는 것이다
class Car:
    value = "부모클래스 필드값"
    def carMethod(self):
        print("조상클래스 메서드 호출")

class Sedan(Car):
    value = "자식클래스 필드값"
    def carMethod(self):
        super().carMethod()
        print("자식클래스 메서드 호출")
        print("부모클래스 value 값 : ", super().value)
        print("자식클래스 value 값 : ", self.value)

if __name__ == "__main__":
    sedan = Sedan()
    sedan.carMethod()