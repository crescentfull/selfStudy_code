'''
1. 지역변수 : 함수안에서 선언되는 변수
2. 전역변수 : 함수 외부에서 선언되는 변수, 프로그램 종료시 같이 소멸
3. 인스턴스 변수: 클래스 안에 선언된 변수, 앞에 self. 붙여준다.
'''

class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def add2(self, x):
        # 클래스 내에서 자신의 메소드를 호출하기 위해서도 self.을 붙여준다
        self.add(x)
        self.add(x)
    def __str__(self):
        return print("리스트 : ", self.data)
if __name__ == "__main__":
    bag = Bag()
    bag.add(10)
    print(bag.__str__())
    bag.add2(30)
    print(type(bag.__str__()))