# 딕셔너리 항목 순회하는 법
scores = {"국어":80, "수학":95, "영어":80}
# 키값만 출력되도록 루프를 돌게한다.
print(scores.keys())
print(type(scores.keys()))
for subject in scores:
    print(subject, end=" ")
# >>> 키값만 출력된다.
print()
print(scores.values())
print(type(scores.values()))
for subject in scores.values():
    print(subject, end="")

print()
print(scores.items())
print(type(scores.items()))
for subject in scores.items():
    print(subject, end=" ")

print("-----------------------")
#딕셔너리 함축(dictionary comprehension)
triples = {x*x*x for x in range(6)}
print(type(triples))
print(triples)

print("-------------------")
# 딕셔너리 정렬(dictionary sort)
# 파이썬에서 딕셔너리는 근본적으로 요소들이 순서가 없기 때문에 순서대로 저장하지 않는다.
dic1 = {"bags":1, "books":5, "bottles":4, "coins":7,"cups":2}
print(dic1)
# 딕셔너리를 리스트로 변환함
li1 = list(dic1)
print(list(dic1)) # 키값만 출력
print(li1)
# 딕셔너리의 키를 정렬하고자 한다면 내장함수인 sorted() 함수를 이용하면 된다.
li2 = sorted(dic1)
print(sorted(dic1))
print(li2)
print("------------------------------")
# 딕셔너리의 값을 정렬하고자 한다면 values()함수와 sorted()함수를 같이 사용하면 된다

print(dic1)
li3 = sorted(dic1.values())
print(sorted(dic1.values()))
print(li3)

print("-------------------------")
# 딕셔너리의 값에 따라서 키들을 정렬하고 싶은 경우에는 sorted()에 요소들을 비교할 때
# 사용하는 키를 지정해주면 된다.
print(sorted(dic1, key=dic1.__getitem__))
print(dic1.__getitem__)