# 사용자로부터 정수를 입력받아서 소수를 판별하는 함수 is_prime()을 작성해보자
# 숫자가 1과 나눠어서 떨어진다면 소수라고 한다...
num = int(input("숫자를 입력하여주시오 : "))
def is_prime(num):
    for i in range(2,num):
        temp = True
        if (num%i) == 0:
            temp = False
        else:
            temp = True
        return temp
print("입력한 값은 : ",is_prime(num))