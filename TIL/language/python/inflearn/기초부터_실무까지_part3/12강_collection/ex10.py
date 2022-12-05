# collection Counter 메서드 실습

# update() : Counter의 값을 갱신하는 것을 의미

from collections import Counter
# 문자열
count = Counter()
print(count)
count.update("안녕하세요")
print(count)
count.update({"안":3, "요":5, "가":3})
print(count)
print(list(count.elements()))

# most_common(n) : 입력된 값의 요소들 중에서 빈도수가 높은 순으로
# 상위 n 개를 리스트 안에 튜플 형태로 반환하는 메서드
print("---------------------------")
count = Counter("apple, orange, grape")
# 매개변수를 주지 않았을 떄는 전체 문자열을 대상으로 값과 빈도수를 출력
print(count.most_common())
# 매개변수를 주어 졌을떄
print(count.most_common(5)) # 빈도수가 높은 순서별로 n개 만큼 출력

# suvstract() : 단어 그대로 요소의 값을 빼는 것을 의미한다.
# 요소가 없는 경우에는 음수의 값을 출력한다.
print("---------------------------")
c1 = Counter("반갑습니다 안녕하세요.")
c2 = Counter("반갑다. 친구야")
c1.subtract(c2)
print(c1)

print("---------------------------")
# Counter()는 산술/집합 연산이 가능하다
# 덧셈
c1 = Counter(["a","b","c","d","a"])
c2 = Counter("apple")
print(c1)
print(c2)
print(c1 + c2)

# 집합, Counter 모듈의 교집합 및 합집합의 출력하는 기능
print("---------------------------")

c1 = Counter("abcdefg")
c2 = Counter("abcd가나다라")
# 교집합을 하고자 할 때는 & 연산자를 사용한다.
print("교 : ", c1 & c2)
# 합집합을 하고자 할 떄는 | 연산자
print("합 : ", c1 | c2)

print("---------------------------")
# Counter()는 산술/집합 연산이 가능하다
# 덧셈
c1 = Counter([1,2,3,4,5])
c2 = Counter([1,2,3,4,6])
print(c1)
print(c2)
print(c1 + c2)