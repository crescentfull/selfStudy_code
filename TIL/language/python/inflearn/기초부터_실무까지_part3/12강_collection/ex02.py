# deque와 list의 성능테스트 비교
from collections import deque
import time  # 성능테스트를 하기 위해서 time 모듈을 가지고 옴
# 아무런 요소가 없는 deque를 생성함
deque_test = deque()
start = time.time() # 시작시간을 저장

for i in range(10000000):
    deque_test.append(i)

end = time.time()
print("deque append : ", end - start)

# 빈 리스트를 생성함
list = list()
start = time.time()
for i in range(1000000):
    list.append(i)

end = time.time()
print("list append 시간 : ", end - start)