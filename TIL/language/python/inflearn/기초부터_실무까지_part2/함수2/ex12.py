# 무명함수(익명함수, anonymous function)에 대한 실습
# 무명함수는 함수명이 없고, 구현부만 존재한다. 파이썬에서는 무명함수를 만들때 lambda키워드로 만들 수 있다.
# 무명함수는 print()등과 같은 일반함수를 호출할 수가 없다. 오직 계산만 가능하다.
# !!!! 전역변수를 참조할 수 없다.

# lambda 인수1, 인수2 : 수식 <-- 문법

def main():
    print("두 수의 합",get_sum(1,5))
    print("두 수의 합",get_sum(10,50))
    # 람다 키워드를 이용햐여 sum() 함수 만들기
    # 람다 함수는 코드 안에 함수를 포함하는 어느 곳이든 사용가능하다.
    # 가장 많이 사용하는 곳은 gui 프로그램에서 이벤트를 처리하는 콜백 함수 형태이다.
    sum = lambda x,y:x+y
    print("람다이용 두수의 합",sum(100,5))
    print("람다이용 두수의 합",sum(10,5))
    
    #람다식으로 구성된 리스트 데이터
    li = [ lambda x:x**2,lambda x:x**3,lambda x:x**4]
    for i in li:
        print(i(10))
    #!! 람다 함수안에서 변수 값에다가 값을 지정해줄 수는 없다.
    # lambda x=10,y:x+y  ERROR햣

def get_sum(x,y):
    return x+y


main( )