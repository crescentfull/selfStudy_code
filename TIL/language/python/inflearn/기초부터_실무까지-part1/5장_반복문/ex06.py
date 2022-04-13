# 피보나치 수열을 구하는 프로그램을 만드시오
# 피보나치 수열이란 앞의 2개의 수를 더해서 다음 수를 결정짓는 수열
# 예) 사용자로부터 13을 입력받고 난 뒤 피보나치 수열의 값 : 1 1 2 3 5 8

n1 = 1
n2 = 1
n3 = 1

fi = int(input("피보나치 수열을 만들 정수를 입력하세요 : "))
for i in range(1,fi):
    if i < 3:
        n3 = 1
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    #사용자로부터 입력받은 값보다 작은 수만 출력하게끔 하였다.
    if n3 < fi:
        print(n3, end=" ")        
