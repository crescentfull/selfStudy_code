# 사용자로부터 달을 입력받아서 입력한 달의 일수를 구하는 프로그램을 작성하기

month = int(input("월을 입력하세요 : "))

if month == 2:
    print(month, "월의 일수는 28일")
elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
    print(month,"월의 일수는 30일")
else:
    print(month,"월의 일수는 31일")