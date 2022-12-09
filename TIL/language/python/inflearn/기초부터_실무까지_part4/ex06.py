# 은행계좌에 돈을 저금할 수 있고 인출을 할 수도 있다. 은행 계좌를 간단하게
# 클래스로 정의해보자. 은행계좌(Acoount)는 현재 잔액(balance)을 필드로 선언하고
# 기본생성자를 작성하고 입금(deposit) 메소드와 출금(withdraw)메서드를 작성
'''
출력결과
통장에 1,000,000원이 입금됨
현재잔액 : 1,000,000원
통장에 200,000원이 출금됨
현재잔액 : 800,000원
'''

class Account:
    __balance = 0
    
    def __init__(self):
        self.__balance = 0
    
    # getter()
    def getBalance(self):
        return self.__balance
    
    # 입금
    def deposit(self, amount):
        self.__balance += amount
        print(f"{format(amount, ',')} 원 입금되었습니다.")
        print(f"현재 잔액 : {format(self.getBalance(), ',')} 원")
    
    #출금
    def withdraw(self, amount):
        self.__balance -= amount
        print(f"{format(amount, ',')} 출금되었습니다.")
        print(f"현재 잔액 : {format(self.getBalance(), ',')} 원")
        
if __name__ == "__main__":
    account = Account()
    account.deposit(100000000)
    account.withdraw(300000)