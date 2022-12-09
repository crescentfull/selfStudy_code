# 클래스 변수와 인스턴스 변수의 다른 예제
class Card:
    kind = ""
    number = 0
    width = 100 # 클래스변수
    height = 250
    
    def __init__(self, kind, number):
        self.kind = kind
        self.number = number
    
    def __str__(self):
        print("kind : ", self.kind)
        print("number : ", self.number)
        print("width : ", Card.width)
        print("height  : ", Card.height)
        
if __name__ == "__main__":
    card1 = Card("다이아몬드", 10)
    card1.__str__()
    card2 = Card("스페이드", 11)
    card2.__str__()