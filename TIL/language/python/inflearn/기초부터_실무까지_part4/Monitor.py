# 매개변수가 있는 생성자
class Monitor:
    # fields
    company = ""
    inch = 0
    price = 0
    color = ""
    
    # 매개변수가 4개 존재하는 생성자
    def __init__(self, company, inch, price, color):
        # self.company는 멤버변수를 칭하는 것, company는 외부에서 생성자를 호출할때 매개변수값으로 들어오는 것을 의미한다.
        self.company = company
        self.inch = inch
        self.color = color
        self.price = price
        
    def __str__(self):
        print("제조사 : ", self.company)
        print("인치 : ", self.company)
        print("제조사 : ", self.company)
        print("제조사 : ", self.company)