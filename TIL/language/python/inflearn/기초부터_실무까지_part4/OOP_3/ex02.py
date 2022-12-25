# 다중상속 실습
class Person:
    def __init__(self):
        print("I'm human")
    def greeting(self):
        print('Person클래스의 greeting메서드 호출')

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        print("I'm student")
    
    def greeting(self):
        print('Student클래스의 greeting메서드 호출')

class Worker(Person):
    def __init__(self):
        Person.__init__(self)
        print("I'm employee")

    def greeting(self):
        print('Worker클래스의 greeting메서드 호출')
        
# 다중상속
class PartTimer(Student, Worker):
    def __init__(self):
        Student.__init__(self)
        Worker.__init__(self)
        print("i'm partimer")
        
    # def greeting(self):
        # print('Parttimer클래스의 greeting메서드 호출')
        
if __name__== "__main__":
    parttimer = PartTimer()
    parttimer.greeting()
    # 다이아 몬드 상속문제점은 같은 이름의 멤버가 있다면 자식클래스에서 해당메서드를 오버라이딩을 하지 않았다면 도대체 어떤 조상클래스의 메서드가 호출되는지를 알 수가 없다
    # 위와 같은 문제점을 해결하기 위해서 파이썬에서는 메서드 탐색순서(MOR:Method Resolution Order) 기법을 사용한다
    print(PartTimer.mro())