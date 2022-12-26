# 다형성으. 개념은 여러가지 형태를 가질 수 있는 능력이다.
# 보이는 실제모습 혹은 행위는 다른 특징을 지닐 수 있다.
# 형식의 다형성, 메서드의 다형성으로 나뉨

class Animal:
    def __init__(self, name, age, weight, instance):
        self.__name = name
        self.__age = age
        self.__weight = weight
        # 아래 코드는 Animal을 상속받는 독립적인 클래스의 인스턴스를 받는다.
        self.__instance = instance
    def show(self):
        print("이름 : ", self.__name)
        print("종류 : ", self.__instance.d_name)
        print("나이 : ", self.__age)
        print("몸무게 : ", self.__weight)
        
        # 매개변수로 넘어오는 독립 클래스의 메서드인 sound() 각각 호출
        self.__instance.sound()
        print("-"*40)
        
class Tiger():
    d_name = "호랑이"
    def sound(self):
        print("어흥")
class Dog():
    d_name = "개"
    def sound(self):
        print("멍멍")
class Cat():
    d_name = "고양이"
    def sound(self):
        print("냐옹")
        
if __name__ == "__main__":
    ani1 = Animal("빠르",8,180,Tiger())
    ani1.show()
    ani2 = Animal("아롱이",4,8,Dog())
    ani2.show()
    ani3 = Animal("또치",2,6,Cat())
    ani3.show()