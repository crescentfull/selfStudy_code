# shape 클래스 실행 파일
from Rectangle import *

def screenLeftClick(x, y):
    rect = Rectangle(x, y)
    rect.drawShape()
    
if __name__ == "__main__":
    turtle.title("클래스를 이용한 사각형 그리기")
    turtle.onscreenclick()