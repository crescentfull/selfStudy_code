# 조건문의 실습(if - else 구문, if 구문)
score = 60

# 수식(관계식) 다음에 : 기호는 인터프리터에게 아직 문장이 끝나지 않음을 알리는 기호
# if-else 구문은 50%로의 확률, '모아니면 도'의 경우에 사용
if score >= 60 :
    print("합격")
else:
    print("불합격")
    
#파이썬에서는 수식(관계식)을 나타내고자 할 때, 괄호()를 사용해도 되기는 하나 웬만하면 괄호를 쓰지 않고 수식을 표현
#왜? warning 창 뜬다

age = int(input("나이를 입력하세요 : "))
if age >= 19:
    print("주류 구입이 가능한 연령입니다")
else:
    print("아직 미성년자라 주류 구입이 안됩니다.")