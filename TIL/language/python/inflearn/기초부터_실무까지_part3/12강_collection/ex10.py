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