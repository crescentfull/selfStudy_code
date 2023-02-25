# 두자리 양수 입력받는 프로그램
print('2자리 양수를 입력하세요.')
while True:
    no = int(input('값을 입력하세요 : '))
    if no >= 10 and no <= 99:
        break
print(f'입력받은 양수는 {no}이다')