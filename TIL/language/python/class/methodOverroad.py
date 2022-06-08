class Person:
    def __init__(self, name):
        self.name = name
    
    def work(self):
        print(self.name + " work hard")
        
# method override (메소드 재정의) 같은 함수명을 덮어쓴다고 생각해
class Student(Person):
    def work(self):
        print(self.name + " study hard")
        
student1 = Student('song')
student1.work()