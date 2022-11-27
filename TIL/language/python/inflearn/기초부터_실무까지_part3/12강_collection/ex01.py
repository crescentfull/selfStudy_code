# collections 모듈이란 기존에 배웠던 자료구조(리스트, 큐, 스택, 튜플, 딕셔너리) 좀 더 확장하여 제작된 파이썬의 내장 모듈
# 1) deque 데크 ,double-ended queue - 양방향으로 IO가 가능한 큐
# 스택과 큐를 모두 지원하는 모듈

from collections import deque
deque_list = deque()
print(deque_list)

for i in range(5):
    deque_list.append(i)
print(deque_list)
# deque에 있는 요소들을 삭제하기
# print(deque_list.pop(0)) # deque에서는 pop(0)인 것이 지원안됨
# deque에서는 스택도 지원하는 모듈이므로 pop() 사용하면 늦게 들어간 데이터부터 삭제됨을 알 수가 있다.

print(deque_list.pop())
print(deque_list.pop())
print(deque_list.pop())
print(deque_list)

print("---------------------")
# appendleft() 메서드 사용 : 새로운 요소들을 왼쪽부터 입력되게 하여 먼저 들어간 값부터 출력될 수 있도록 한다.
# 양방향으로 입력이 가능한 것이다.
 
deque_list.clear()
print(deque_list)
for i in range(5):
    deque_list.appendleft(i)
    print(deque_list)
print(deque_list)

print(deque_list.pop())
print(deque_list.pop())
print(deque_list.pop())
print(deque_list)

print("----------------------------")
# deque 모듈은 원형연결리스트(linked list)의 특성 지원
# 연결 리스트는 데이터를 저장할 때, 요소의 값을 한 쪽으로 연결한 후, 요소의 다음 값의 주소값을 저장하여 연결하는 기법이다.
deque_list.clear()
print(deque_list)
for i in range(5):
    deque_list.appendleft(i)
print(deque_list)
# rotate(n) : 요소들을 n만큼 회전해주는 메소드
# 단, 양수이면 시계방향(오른쪽) 회전을 하고 음수이면 반시계방향(왼쪽)으로 이동
deque_list.rotate(1)
print(deque_list)


print("----------------------------")
# reversed()
print(deque.reverse(deque_list))
# reversed() 메소드는 기존 요소를 반대로 지정할 수 있게 하는 것이다.

print("----------------------------")
# extend() : 리스트를 우측에 통쨰로 붙인다, 
# extendleft() : 리스트를 좌측에 통째로 붙인다.
deque_list.extend([5,6,7])
print(deque_list)
deque_list.extendleft([5,6,7])
print(deque_list)

print("----------------------------")
deque_list.clear()
print(deque_list)
basedata = ["a","b","c","d","e"]
# maxlen 매개변수는 deque의 사이즈를 고정시켜버리는 인자값이다.
deque_list = deque(basedata, maxlen=3)
print(deque_list)
# popleft() 메소드는 deque에서 요소의 왼쪽에 있는 것을 삭제한다.
print(deque_list.popleft())
print(deque_list)