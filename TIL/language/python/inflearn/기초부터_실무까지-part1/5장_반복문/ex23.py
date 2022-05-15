# 사용자로부터 전화번호를 입력받다 보면 "-"를 적는 경우가 많다.
# "-"을 합하여 입력 받도록 하고 출력을 할 때는 "-"삭제를 한 문자열을 출력하는 프로그램을 작성하시오

mobile = input("휴대폰 번호 입력 ( '-' 포함) : ")
res = ''

if 11<len(mobile)<14:
    for i in mobile:
        if i != '-':
            res += i
    print(res)
else:
    print("잘못된 번호입니다")