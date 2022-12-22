from shape import *

# 자식 클래스 Rectangle 정의
class Rectangle(Shape):
    width = 0
    height = 0
    def __init__(self, cx, cy):
        Shape.__init__(self) # 조상클래스의 생성자 호출
        self.cx = cx
        self.cy = cy
        # 사각형의 너비, 폭을 임의의 수로 결정
        self.width = random.randrange(20,100)
        self.height = random.randrange(20,100)
        print("width : ", self.width)
        print("height : ", self.height)
        
    # 부모클래스 drawShape() 오버라이딩
    def drawShape(self):
        # 사각형 그리기
        sx1, sy1 = 0, 0 # 좌측 상단의 좌표값
        sx2, sy2 = 0, 0 # 우측 하단의 좌표값
        
        sx1 = self.cx - self.width//2
        sy1 = self.cy - self.height//2
        sx2 = self.cx - self.width//2
        sy2 = self.cy - self.height//2
        print(f"sx1,sy1 = {sx1},{sy1}, sx2,sy2 = {sx2},{sy2}")
        self.setPen() # 팬의 색상과 두께를 부모클래스의 메서드 호출
        self.myTurtle.penup()   # 펜을드는 메서드
        self.myTurtle.goto(sx1,sy1) # 펜을 좌측 상단으로 이동
        self.myTurtle.pendown() # 펜을 내리는 메서드
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)
    
    