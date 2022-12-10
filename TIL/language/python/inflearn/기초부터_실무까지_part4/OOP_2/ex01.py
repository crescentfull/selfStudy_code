'''
인스턴스가 함수의 인자값으로 전달될 때는 함수에서 인스턴스의 값을 변경할수 있다.
그 이유는 인스턴스는 함수에 매개변수로 전달될 때 참조(주소)값이 전달이 되어서 변경이 가능하다.
리스트를 생각해보자
'''

# 사각형 클래스 정의
class Rectangle:
    # side=0 는 매개변수의 값이 주어지지 아니할때 0으로 초기화
    def __init__(self, side=0):
        self.side = side
    # 정사각형의 면적을 출력하는 메소드
    def getArea(self):
        return self.side * self.side
    
    #
    def printArea(rectangle, cnt):
        print("변의 길이 \t면적")
        while cnt >= 1:
            print("\t",rectangle.side, "\t", rectangle.getArea())
            rectangle.side += 1
            cnt -= 1

if __name__ == "__main__":
    rectangle = Rectangle()
    cnt = 5
    rectangle.printArea(cnt)
    print("정사각형의 한 변의 길이 : ", rectangle.side)
    print("반복획수 : ", cnt)