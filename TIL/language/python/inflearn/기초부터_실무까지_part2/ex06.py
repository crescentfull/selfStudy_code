# 간단한 사칙연산 계산기 만들기
x,y = map(int,input("숫자 2개 입력 : ").split(","))
# 더하기
def sum(x,y):
    return x+y
# 빼기
def minus(x,y):
    return x-y    
# 나누기
def divide(x,y):
    return x/y #( // => 정수만 )
# 곱하기
def multiple(x,y):
    return x*y

option = input("연산자를 선택하시오 (+,-,%,*) : ")

if option == '+':
    print("덧셈 : ",sum(x,y))
elif option == '-':
    print("뺄셈 : ",minus(x,y))
elif option == '%':
    print("나눗셈 : ",divide(x,y))
elif option == '*':
    print("곱셈 : ",multiple(x,y))
else:
    print("잘못된 연산자를 입력하였습니다")