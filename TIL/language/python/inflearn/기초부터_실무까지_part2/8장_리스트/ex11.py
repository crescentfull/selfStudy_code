# 리스트 컴프리헨션
# 리스트 컴프리헨션은 수학에서 집합을 정의하는 것과 비슷하다

# 일반적 코드 
li =[]
for x in range(1,11):
    li.append(x**2)
print(li)

# 리스트 컴프리헨션
# 출력식 + 반복문 + 조건문(옵션)
li2 = [x**2 for x in range(1,11)]
print(li2)

# 조건문이 붙는 리스트 컴프리헨션
odd_li = [x**2 for x in range(1,11) if (x % 2) == 1]
even_li = [x**2 for x in range(1,11) if (x % 2) == 0]
print(odd_li)
print(even_li)

#반복문 2번 사용해서 구구단 값 출력
mutiplication_table = [x*y for x in range(2,10) for y in range(1,10)]
print(mutiplication_table)