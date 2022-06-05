# 함수가 리턴값이 없는 경우에 대한 예제
def printInfo(name,age):
    print("===========")
    print("name : ", name)
    print("나이 : ", age)
    print("===========")
    return #리턴 값이 없다면 리턴문 뒤에 아무것도 적지 않는다.

print("이름과 나이를 입력해주세요.")
end_Input = 'y'
while True:
    if end_Input == 'n':
        break
    elif end_Input == 'y':
        name = input("회원명을 입력해주세요 : ")
        age = int(input("회원 나이 입력 : "))
        printInfo(name,age)
        end_Input = input("continue? y/n : ")
    else:
        print("잘못 입력하였습니다.")
        end_Input = input("continue? y/n : ")