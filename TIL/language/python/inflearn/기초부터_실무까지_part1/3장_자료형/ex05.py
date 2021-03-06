## 문자열의 연결
# + 연산자는 문자열 사이에 들어가면 문자열을 연결해주는 역할을 한다.
first_name = " Eun Hyuk"
last_name = "Shin"
name = last_name + first_name
print(name)

# 파이썬의 모든 데이터에는 데이터 타입이 존재한다. 아래 소스코드에서 확인을 하면 "person"은 문자열이고 100은 int타입이다. 타입으 일치가 되지않아 합치면 에러가 난다
# 그때는 100을 str(100)으로 문자열 변환을 시켜주면 해결된다. 하지만 문자로 된 문자열은 int타입으로 변환은 불가능하다!
temp = "person" + str(100)
# 실수일때는 float()을 사용하면 된다.

##문자열의 반복
# 문자열에서 * 연산자를 이용하면 그만큼 반복이 된다.
arrow = "->" * 10
print(arrow)

# %s(형식 지정자)
# %s는 문자열이나 숫자값을 변수에 대입해서 자주 변경이 있을 경우에 이런 형식을 지정하여
# 상황에 맞게끔 출력을 하도록 하면 된다.
price = 1000
print("price : %s" % price)

time = "13:00"
print("price : %s" % time)
#! %s를 2개 이상을 사용하고자 할 때는 해당하는 갯수만큼 소괄호로 묶어서 지정해줘야한다.
temp = "현재 시간은 %s시 %s분 %s초 입니다"
print(temp %(10,10,10))