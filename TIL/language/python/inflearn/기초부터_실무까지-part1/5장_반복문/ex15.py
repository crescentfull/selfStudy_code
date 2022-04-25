# 사용자로부터 상품금액을 입력받아서 상품의 총 가격을 계산하는 프로그램 만들기
# 사용자가 몇 개의 상품을 살지 모르니깐 무한루프를 이용하고, 사용자가 "끝"이라고 입력을 하면 루프를 종료하게 조건을 준다
from operator import eq
total = 0
price = ""

while True:
    price = input("상품 금액을 입력하세요.('끝' 입력하면 종료) : ")
    if eq(price, "끝"):   # if price == "끝"이랑 동일. operator import해줘야한다.
        print("상품의 총 가격 : "+str(total)+"원")
        break
    total += int(price)