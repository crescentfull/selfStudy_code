from re import A


def test(n1,n2):    # 함수의 매개변수도 지역변수의 일종
    global a        # 함수 내에서 전역변수 a를 사용하겠다라고 명시
    a = 20          # 전역변수 값 변경
    n1 = n2
    n2 = n1
    b = 10
    print('함수 실행 : ', a, b, n1, n2)
    
a = 1
b = 20
n1 = 77
n2 = 88
test(n1,n2)
print(a, b, n1, n2)