# 리스트에 대한 실습
# 리스트에 정의 : 여러개의 값을 모아서 하나의 변수에 저장할 수가 있는 데이터 타입이다.
# 리스트는 []안에 값을 저장한다.
city = ["서울", "부산", "대구", "광주", "인천"]
# 리스트의 길이를 알아내고 싶을 때에도 역시 len()을 사용하면 된다.

print(len(city)) 
print(city)
print(city[2])
# 리스트는 아래와 같이 해당하는 인덱스의 값이 변경 가능한 객체이다.
city[1] = "전주"
print(city)
# 리스트는 정수, 문자열에 국한되지 않고 여러 개의 값을 저장 할 수가 있다.
temp = ["대구", "부산", 100, 10.888]
print(temp)

# 한 사람의 정보를 출력
name = input("이름 : ")
age = int(input("나이 : "))
address = input("주소 : ")
tall = int(input("키 : "))
weight = int(input("몸무게 : "))

person = [name, age, address, tall, weight]
print(person) 