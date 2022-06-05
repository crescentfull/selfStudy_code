# 함수가 리턴값이 없는 경우에 대한 예제
def printInfo(name,age):
    print("===========")
    print("name : ", name)
    print("나이 : ", age)
    print("===========")
    return

print("이름과 나이를 입력해주세요.(입력종료 :  q)")
while True:
    name = input("회원명을 입력해주세요.")
    age = int(input)