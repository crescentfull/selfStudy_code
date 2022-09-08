# 사용자로부터 10진수를 입력받아서 2진수 문자열로 변환하는 반환하는 decTobin(num)을 작성
def decTobin(num):
    binary = ''
    
    while num != 0:
        value = (num%2)==0
        if value == 0:
            binary = '0' + binary
        else:
            binary = '1' + binary
        num = num//2
        print(num)
    return print(binary)
decTobin(12)

print(bin(12)) #2진법
print(oct(12)) #8진법
print(hex(12)) #16진법