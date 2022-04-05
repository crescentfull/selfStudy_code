# 쇼핑몰에서 물건을 구매할 때, 구입액이 5마원 이상이면 5%의 할인을 해준다.
# 사용자에게 구입 금액을 입력받고 최종적으로 할인 금액과 지불금액을 출력하는 프로그램

buy_price = int(input("구입금액 : "))
if buy_price >= 50000:
    discount = round(buy_price*0.05)
    price = round(buy_price - (discount))
    print("5만원 이상이므로 5%할인 해줍니다","\n할인 금액 : ",discount,"\n최종 금액 : ", price)
else:
    print("5만원 미만이므로 할인율이 없습니다.","\n최종금액 : ",buy_price)