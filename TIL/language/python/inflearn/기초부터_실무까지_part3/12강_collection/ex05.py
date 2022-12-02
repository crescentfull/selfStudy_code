# defaultdict 모듈은 딕셔너리의 요소를 생성할 때, 키에 기본 값을 지정하는 방법
# 일반적인 딕셔너리를 생성하고 키의 값으로 요청값을 알아낼 수 있다.
dic = dict()
print(dic)

# print(dic["a"]) # KeyError
print(dic.get("a"))

from collections import defaultdict

# defaultdic 는 아직 모르는 키에 대해서 기본 값을 0으로 지정
dic = defaultdict(lambda : 0) # lambda를 이용하여 0을 리턴하도록 함
print(dic["a"])
print(dic["b"])
print(dic)

print("--------------------------------")
dic.clear()
dic = defaultdict(int) # 키에 대한 값을 int형으로 설정
dic["a"] += 100 # 해당 키에 대한 값에다가 연산을 할 수도 있다.
print(dic["a"])
print(dic["b"])
print(dic["100"])
print(dic)

print("--------------------------------")
dic.clear()
dic = defaultdict(float) # 키에 대한 값을 float형으로 설정
print(dic["a"])
print(dic["b"])
print(dic["100"])
print(dic)

print("--------------------------------")
dic.clear()
dic = defaultdict(str) # 키에 대한 값을 str형으로 설정
print(dic["a"])
print(dic["b"])
print(dic["100"])
print(dic)