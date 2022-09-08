# 일회용 패스워드 생성기를 만들어서 3개의 패스워드를 생성하여 출력해보라
# 패스워드 길이는 6자리

import random

def randomPassword():
    num_str = "0123456789"
    num = random.sample(range(1,10),6) # random.sample() 중복 숫자 알아서 배재해준다
    res = [str(i) for i in num]
    res = ''.join(res)
    return int(res)

for i in range(1,4):
    print(randomPassword())