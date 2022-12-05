# counter 모듈은 시퀀스 자료형의 데이터의 값의 갯수를 딕셔너리 형태로
# 반환해주는 자료구조이다. 
# 같은 값이 몇 개가 존재하는지 쉽게 알아보고자 할 때 사용하면 편리하다

from collections import Counter
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