
class Figure:
    def __init__(self, name, color):
        self.name  = name
        self.color = color
        
class Quadrangle(Figure): # 부모클래스(자식클래스) / 부모클래스를 자식클래스에 상속시켜준다.
    def set_area(self, width, height):
        self.width  = width
        self.height = height
    
    def get_info(self):
        print(self.name, self.color, (self.width * self.height))

#객체생성       
square = Quadrangle('dave','blue') # 객체생성
#객체실행
square.set_area(5,5) #자식클래스 함수 적용
square.get_info() #info 함수호출

print(issubclass(Quadrangle, Figure)) # issubclass 클래스간의 관계확인 위해서 쓴다. 이경우 Quadrangle가 Figure의 자식클래스인지 확인해줌

#isinstance(객체,클래스) 객체와 클래스간의 관계확인을 위해서 사용한다
#객체생성
fiqure1 = Figure('figure1','black')
square = Quadrangle('square','red')
print(isinstance(fiqure1,Figure))
print(isinstance(square,Quadrangle))

##################################################3
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(self.name + ' studies hard')

class Teacher(Person):
    def teach(self):
        print(self.name + ' teaches hard')
        
# 객체생성
student1 = Student('song')
teacher1 = Teacher('kim')
# 객체실행
student1.study()
teacher1.teach()
