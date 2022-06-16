# instance method : 해당 객체안에서 호출(self.메서드명을 의미)
# - 해당메서드를 호출한 객체에만 영향을 미친다
# - 객체 속성에 접근이 가능하다

# static method : 객체와 독립적이지만, 로직상 클래스내에 포함되는 메서드
# - self 파라미터를 갖고있지 않음
# - 객체 속성에 접근이 불가하다
# - 정적 메서드는 메서드 앞에 @staticmethod 라는 decorator를 넣어줘야한다
# 클래스명.정적메서드명 또는 객체명.정적메서드명 둘다 호출이 가능하다

from turtle import circle


class Figure:
    #생성자(initializer)
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #메서드
    def clac_area(self):
        return self.width * self.height
    #정적메서드(Figure에 너비와 높이가 같은 도형은 정사각형임을 알려주는 기능)
    @staticmethod
    def is_square(rect_width, rect_height):
        if rect_width == rect_height:
            print("정사각형")
        else:
            print("no 정사각형")
#호출
figure1 = Figure(2,3)
figure1.is_square(5,5)
Figure.is_square(4,5)

##
print("****************************************")
## classmethod 
# - self파라미터 대신 cls파라미터
# - 클래스 변수 접근가능하며 cls.클래스명으로 액세스가능 단!객체 속성/메서드는 불가!!
# - 클래스 메서드는 메서드앞에 @classmethod를 넣어줘야한다
# 클래스명.정적메서드명 또는 객체명.정적메서드명 둘다 호출이 가능하다
class Figure1:
    count = 0 #클래스변수
    # 생성자(initializer)
    def __init__(self, width, height):
        #self.*: 인스턴스변수
        self.width = width
        self.height = height
        #클래스변수 접근
        Figure1.count += 1
    #메서드
    def calc_area(self):
        return self.width * self.height
    #클래스메서드
    @classmethod 
    def print_count(cls):
        return cls.count
#호출
figure1 = Figure1(2,3)
figure2 = Figure1(4,5)
print(Figure1.count)
print(Figure1.print_count()) #2
print(Figure1.print_count()) #2

##
print("****************************************")
##
# 차이점
class Diff:
    @classmethod
    def set_name(cls, name):
        cls.name = name
        
class Circle(Diff):
    pass

Diff.set_name("diff")
print(Diff.name, Circle.name)
Circle.set_name("circle")
print(Diff.name, Circle.name)
##
print("****************************************")
##
class Diff2:
    @staticmethod
    def set_name(name): #self 필요 없다
        Diff2.name = name #안에서 정의할려면 해당클래스명.변수명

class Circle2(Diff2):
    pass

Diff2.set_name("diff2")
print(Diff2.name, Circle2.name)
Circle2.set_name("circle")
print(Diff2.name, Circle2.name)