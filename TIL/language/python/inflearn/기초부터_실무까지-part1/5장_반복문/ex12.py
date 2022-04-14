# while 문의 실습
# while문은 조건을 정해놓고 반복을 하는 구조이다.

i = 0
while i < 5:
    i += 1
    print("반갑습니다")
print("종료")

i = 0
while i<10:
    i += 1
    print(i, end=" ")
print(" ")
#1~10까지의 누계합
i = 0
sum = 0
while i<=10:
    sum += i
    i += 1
print("합 : ",sum)
#팩토리얼
i = 1
res = 1
while i <= 10:
    res *= i
    i += 1
print("10! : ",res)

#구구단 3단 구현
i = 1
while i <= 9:
    print("3 * %d = %2d" %(i, 3*i)) # %d 할때 %뒤에오는 숫자들은 설정만큼의 자릿수를 차지하게 해준다.
    i += 1

# 1~100까지의 3의 배수만 누적값을 구하는 예제
i = 1
sum = 0
while i <= 100:
    if i % 3 == 0:
        sum += i
    i += 1
print(sum)

# 각 지릿수 합을 계산하는 예제
num = 1234
sum = 0
while num >0:
    digit = num%10
    sum += digit
    num = num // 10
    print(digit)
    print(num)

print("답 : ",sum)