# 다형성 실습
class Product:
    price = 0
    bonusPoint = 0
    # 매개변수를 가진 생성자
    def __init__(self, price):
        self.price = price
        # 보너스 점수는 제품 가격에 10프로를 적립함
        self.bonusPoint = int(self.price/10.0)
        
class Tv(Product):
    def __init__(self, price):
        super().__init__(price) # 조상클래스의 생성자 호출
    # 구매목록 파악    
    def __str__(self):
        return "Tv"
class Computer(Product):
    def __init__(self, price):
        super().__init__(price) # 조상클래스의 생성자 호출
    # 구매목록 파악    
    def __str__(self):
        return "Computer"
class Audio(Product):
    def __init__(self, price):
        super().__init__(price) # 조상클래스의 생성자 호출
    # 구매목록 파악    
    def __str__(self):
        return "Audio"

# 물건을 사는 독립적 클래스
class Buyer:
    money = 1000
    bonusPoint = 0
    # 매개변수 다형성
    def buy(self, product):
        # 가진 돈보다 제품의 가격이 비싼 경우
        if self.money < product.price:
            print("잔액 부족")
            return
        # 가진 돈에서 구입한 제품의 가격을 빼준다
        self.money -= product.price
        # 제품의 보너스 점수를 추가한다
        self.bonusPoint += product.bonusPoint
        print(product.__str__()+"구매")

if __name__ == "__main__":
    buyer = Buyer()
    tv = Tv(300)
    computer = Computer(100)
    audio = Audio(50)
    
    buyer.buy(tv)
    buyer.buy(computer)
    buyer.buy(audio)
    # 생성된 인스턴스를 Buyer클래스의 buy()메서드의 매개변수 값으로 대입
    print("잔액 : ", buyer.money)
    print("잔여 보너스 포인트 : ", buyer.bonusPoint)
    
    # 형식의 다형성
    buyer.buy(Tv(300))
    buyer.buy(Computer(100))
    print("잔액 : ", buyer.money)
    print("잔여 보너스 포인트 : ", buyer.bonusPoint)