# instance method : 해당 객체안에서 호출(self.메서드명을 의미)
# - 해당메서드를 호출한 객체에만 영향을 미친다
# - 객체 속성에 접근이 가능하다

# static method : 객체와 독립적이지만, 로직상 클래스내에 포함되는 메서드
# - self 파라미터를 갖고있지 않음
# - 객체 속성에 접근이 불가하다
# - 정적 메서드는 메서드 앞에 @staticmethod 라는 decorator를 넣어줘야한다
# 클래스명.정적메서드명 또는 객체명.정적메서드명 둘다 호출이 가능하다

from turtle import width


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