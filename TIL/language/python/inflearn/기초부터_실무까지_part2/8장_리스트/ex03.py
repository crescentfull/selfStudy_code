# 사용자로부터 강아지의 이름을 저장하였다가 출력하는 프로그램을 작성해보라
# 조건 : 무한루프를 돌면서 엔터키가 입력되면 무한루프를 탈출한다...?

dogs = []

while True:
    name = input("강아지의 이름을 입력하시오(종료시에는 엔터키) : ")
    if name == "":
        break
    dogs.append(name)
    
print("강아지의 이름은",dogs,"입니다.")