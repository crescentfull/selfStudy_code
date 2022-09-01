# 피보나치 수열의 함수만 선언 및 구현 -- 모듈의 형태
# 모듈의 정의 : 함수나 변수들을 모아 놓은 파일
# 모듈이라는 것은 자주 사용될 것으로 예상되는 함수들을 선언 및 구현으로
# 정의를 해놓은 파일이며, 타 프로그램에서 import 키워드로 다른 실행 파일에 도움을 주는 형태의 집합체 이다.

def fibo(n):
    n1 = 0
    n2 = 0
    while n2<n:
        print(n2, end="")
        n1 = n2
        n2 = n1 + n2
        
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1
    return sum