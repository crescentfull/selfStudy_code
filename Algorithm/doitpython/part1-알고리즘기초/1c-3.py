# 두자리 양수 입력받는 프로그램
print('2자리 양수를 입력하세요.')
while True:
    no = int(input('값을 입력하세요 : '))
    if no >= 10 and no <= 99:
        break
print(f'입력받은 양수는 {no}이다')

# 드모르간의 법칙:
# De Morgan's laws
# '각 조건을 부정하고 논리곱을 논리합으로, 논리합을 논리곱으로 바꾸고 다시 전체를 부정하면 원래의 조건과 같다'
# 1. x and y 와 not(not x or not y)의 논릿값은 같습니다.
# 2. x or y 와 not(not x and not y)의 논릿값은 같습니다.