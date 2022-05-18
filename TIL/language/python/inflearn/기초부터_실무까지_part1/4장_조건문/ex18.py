# 주사위 눈을 랜덤으로 발생시켜서 해당하는 숫자를 출력하는 프로그램을 작성
# randint() 함수로 만들어보라

import random

dice = int(random.randint(1,6))
#randint(a,b) => a에서 b까지의 숫자의 범위에서 난수생성
print(dice)

# random() 함수는 0에서 1.0사이의 값을 생성
num = random.random()
print(num)

#randrange(start,stop,step) 함수는 start에서 stop까지 step의 값에 따라서 난수 생성
num = random.randrange(1,100,2)
print(num)
#randrange(a) 0에서 a 미만! 까지의 임의 정수 값 출력
num = random.randrange(9)
print(num)