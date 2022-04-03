#사용자로부터 두 개의 정수를 입력받아서 둘중에서 큰수를 출력하는 프로그램
a = int(input("a입력 : "))
b = int(input("b입력 : "))

answer = 0
if a > b:
    answer = a
    print("a가 더큽니다")
else:
    answer = b
    print("b가 더큽니다")

