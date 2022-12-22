# 조상클래스 shape 정의
import turtle, random

class Shape:
    myTurtle = None
    cx, cy = 0, 0   # 도형의 중심점
    
    # 기본 생성자
    def __init__(self):
        self.myTurtle = turtle.Turtle()
    # 펜 색상과 두께를 무작위로 뽑기
    def setPen(self):
        r = random.random()
        g = random.random()
        b = random.random()
        print("r : ", r)
        print("g : ", g)
        print("b : ", b)
        self.myTurtle.pencolor((r,g,b)) # 펜 색상 지정하기
        penSize = random.randrange(1,20)    # 펜 굵기 랜덤값
        self.myTurtle.pensize(penSize) # 펜의 굴기를 지정
    # Shape 클래스를 상속받는 클래스들을 필요에 의해서 drawShape()를 오버라이딩 할 수 있도록 선언부 선언과 아무런 내용이 없는 구현부를 만들어 두었다.
    def drawShape(self):
        pass