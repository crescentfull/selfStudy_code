#super 자식클래스가 부모클래스의 method를 호출할때
class Person:
    def work(self):
        print('work hard')

class Student(Person):
    def work(self):
        print('study hard')
    
    def parttime(self):
        super().work()

st1 = Student()
st1.work()
st1.parttime()

#self
#self는 현재의 객체를 나타낸다. self.method명 또는 attribute명으로 호출한다.
#java에서는 this라는 키워드를 사용한다.
class Person2:
    def work(self):
        print('work hard')

class Student2(Person2):
    def work(self):
        print('study hard')
    
    def parttime(self):
        super().work()
    
    def general(self):
        self.work()
        
st2 = Student2()
st2.general()