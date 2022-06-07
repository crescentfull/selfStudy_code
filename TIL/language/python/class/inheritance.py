from turtle import width


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
        
square = Quadrangle('dave','blue') # 객체생성
square.set_area(5,5) #자식클래스 함수 적용
square.get_info() #info 함수호출