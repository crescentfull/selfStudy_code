# 정렬과 탐색의 실습
# sort()메소드와 sorted()내장함수의 차이점

# sorted() 내장함수는 원본 리스트를 변경을 시키지 아니하고 정렬된 리스트를 반환한다.
# sorted() 내장함수는 반복가능한 객체들을 다 매개변수로 받을 수 있는 장점이 있다.
a = [4,2,1,5,7,-1]
b = sorted(a)

print(a)
print(b)
print(id(a))
print(id(b))

print("-"*40)
# 리스트만의 메소드인 sort()
x = [1, 4, 2, -10, -99]
y = x.sort()
print(x)
print(y)
# sorted()를 이용하여 매개변수를 딕셔너리를 주면 키값으로 오름차순 정렬이 이루어진다.
print(sorted({3:"D", 2:"B", 5:"B", 4:"E", 1:"A"}))

# key 매개변수 실습
# key=str.lower ==> 대소문자 구별없이
print(sorted("가는 고향 아쉬운 사람 The health not of their but".split(), key=str.lower))
print(sorted("가는 고향 아쉬운 사람 The health not of their but".split(), key=str.lower))
students = [
    ("송영록", 4.4, 20210701),
    ("김김김", 4.1, 20210702),
    ("이쓰리", 3.4, 20210703)
]
print(sorted(students, key=lambda students: students[2]))