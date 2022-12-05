# counter 모듈은 시퀀스 자료형의 데이터의 값의 갯수를 딕셔너리 형태로
# 반환해주는 자료구조이다. 
# 같은 값이 몇 개가 존재하는지 쉽게 알아보고자 할 때 사용하면 편리하다

from collections import Counter
from itertools import repeat, chain
# 문자열을 가지고 리스트 생성
text = list("high school")

print(text)
print(type(text))

count = Counter(text)
print(type(count))

print("------------------------")
# Counter() 객체를 만들 때, 값 = 갯수 와 같은 형태로도 입력 가능
count = Counter(b=2, c=5, a=3)
print(count)
# elements()는 Counter로 주어진 값의 요소에 해당하는 값을 풀어서 반환을 한다.
# 요소는 무작위적으로 반환하며 요소의 수가 1보다 작을 경우에는 elements()는 이를 출력하지 않는다.
# 대,소문자를 구별해서 sorted 정렬
print(sorted(count.elements()))

print(list(repeat([1,2,3], 3)))
print(list(chain.from_iterable(repeat(number, 3) for number in [1,2,3])))

print("---------------------------")
# a = "가"
# b = "나"
# count = Counter("a" == 3, "b" == 5)
# 값 = 갯수형태로 Counter 객체를 만들 때는 문자열은 매개변수로 쓸 수가 없다.
# 문자열 자체를 매개변수로 넣어주는 것은 가능하다.
count = Counter("가나다라마사아")
print(count)
print(sorted(count.elements()))

print("---------------------------")
text = "abcdefg repeat count! you can do it nice to meet you. A Count" \
        "telephone !!!!!".lower().split()
print(text)
print(Counter(text))


print("-------------------")
count = Counter({"가":2, "나":4})
print(count)
print(list(count.elements()))# print(count.elements()) # error list형태로 바꿔줘야함
# 