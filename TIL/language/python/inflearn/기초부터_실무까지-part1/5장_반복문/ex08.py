# 사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램

num = int(input("1~100숫자 입력 : "))
print(f"{num}단 구구단")
for i in range(1,10):
    res = num*i
    print(f"{num} X {i} : ",res)