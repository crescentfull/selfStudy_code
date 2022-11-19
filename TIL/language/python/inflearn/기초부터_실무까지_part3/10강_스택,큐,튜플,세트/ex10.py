# 부분 집합 연산

set1 = {10,20,30}
set2 = {10,20,30}

# 같은지 검사하는 방법(==, !=)

print(set1 == set2)
print(set1 != set2)

set1 = {10,20,30,40,50,60,}
set2 = {10,20,30}
# 부분 집합 판별
# 진상위 집합의 개념 : set2 집합이 set1 집합에 포함되지만 서로 동일하지는 않다.
print(set1 > set2) 
print(set2.issubset(set1))
print(set1 < set2)

# 상위 집합인지 확인하는 방법
print("set1은 set2에 상위집합인가? : ", set1.issuperset(set2))

# 데이터값이 집합에 포함되어  있는가?
set_string = set("hi")
print(set_string)
if "h" in set_string:
    print("yes")
    
# !집합 연산을 할 수 있는 것이 세트 자료구조의 장점이다.
# 합집합
print(set1 | set2) # | 파이프
print(set1.union(set2)) # union()

# 교집합
print(set1 & set2)
print(set1.intersection(set2)) # intersection()

# 차집합
print(set1 - set2)
print(set1.difference(set2))

# all() 중복 없나? any() 중복있나?
# 집합이 첨부터 아에 다른지를 확인하고 싶을 때(같은 요소가 없음)
print(set1.isdisjoint(set2)) # false 같은 요소가 있다~

# set() 에서 pop()은 순서없이 랜덤요소가 제거 된다.
for _ in range(0, len(set1)):
    print(set1.pop(), end=" ")
print()
print("현재 set 크기 ", len(set1))
# 정수의 경우에는 한번 가져온 패턴이 저장되어 계속 진행되지만,
# 문자열을 삭제 및 출력 패턴이 실행될때 마다 달라진다..!
# disgard({요소}) 해당 요소만 삭제