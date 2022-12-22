# shape 클래스 실행 파일
from Rectangle import *

def screenLeftClick(x, y):
    rect = Rectangle(x, y)
    rect.drawShape()
    
if __name__ == "__main__":
    turtle.title("클래스를 이용한 사각형 그리기")
    # 아래 코드는 터틀 그래픽 판에서 마우스 왼쪽 버튼이 클릭이 되는 것을 감지하는 리스너 메서드이다.
    # 1운 왼쪽 버튼, 2는 휠, 3은 우측 버튼
    turtle.onscreenclick(screenLeftClick, 1)
    turtle.done()