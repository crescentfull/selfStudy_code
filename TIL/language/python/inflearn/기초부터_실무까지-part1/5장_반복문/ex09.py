# 사용자로부터 2개의 정수 값을 입력받고 첫번째 입력받은 값에서 두번째 입력받은 값까지
# 3과 4의 배수를 제외한 숫자를 출력하는 프로그램을 작성

a = int(input("first : "))
b = int(input("second : "))

for i in range(a,b+1):
    if (i%3) == 0 and (i%4) == 0:
        continue # continuew는 조건식이 참이면 조건식 아래 아래문장을 실행하지않고 for문으로 다시 이동하여 for문을 실행시킨다.
    print(i)