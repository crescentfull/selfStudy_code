# 매개변수가 있는 생성자
class Monitor:
    # fields
    # __ >> private 
    company = ""
    inch = 0
    price = 0
    color = ""
    

    # 파이썬에서는 1개 이상의 생성자를 만들 수가 없다.
    # 오버로딩 : 영어 뜻으로는 과적하다. 같은 메서드명으로 다른일을 하게끔 만드는 작업
    # 매개변수의 타입과 갯수에 따라서 같은 이름의 메서드라도 다른 메서드가 호출이되는 형태를 지칭

    # 매개변수가 4개 존재하는 생성자    
    def __init__(self, company, inch, price, color):
        # self.company는 멤버변수를 칭하는 것, company는 외부에서 생성자를 호출할때 매개변수값으로 들어오는 것을 의미한다.
        self.__company = company
        self.__inch = inch
        self.__color = color
        self.__price = price
        print("매개변수가 있는 생성자 호출")
    
    # getter 메서드(값만 읽을수 있도록)
    def getCompany(self):
        return self.__company
    def getInch(self):
        return self.__inch
    def getPrice(self):
        return self.__price
    def getColor(self):
        return self.__color
    
    # setter 메서드(멤버변수의 값을 변경시켜주는 메서드)
    # 중요한 것들은 setter를 만들어주면 안된다
    # 외부에서 함부러 변경을 하지 못하게 해야하기 떄문이다.
    def setCompany(self, company):
        self.__company == company
    def setInch(self, inch):
        self.__inch == inch
    def setPrice(self, price):
        self.__price == price
    def setColor(self, color):
        self.__color == color
    
    
    
    # 멤버변수들의 값을 찍어보기 위한 메서드    
    def __str__(self):
        print("제조사 : ", self.getCompany())
        print("인치 : ", self.getInch())
        print("가격 : ", self.getPrice())
        print("색 : ", self.getColor())