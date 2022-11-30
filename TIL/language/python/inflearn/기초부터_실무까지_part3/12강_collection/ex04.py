# 일반 딕셔너리를 정렬하여 OrderDict로 포장하기
dic = {}
dic["z"] = 100
dic["a"] = 200
dic["e"] = 300
dic["d"] = 400
dic["e"] = 500
dic["h"] = 500
dic["j"] = 500
dic["h"] = 500
dic["g"] = 500
dic["1"] = 500
dic["3"] = 500
dic["m"] = 500

# 키값 정렬
# li1 = sorted(dic.keys())
# print(li1)

from collections import OrderedDict

# 넘어오는 t의 값은 딕셔너리의 요소이다.
# 0 인덱스는 키값
def sort_by_key(t):
    print(t)
    return t[1]
    
dic1 = {}
dic1["z"] = 500
dic1["a"] = 200
dic1["e"] = 300
dic1["d"] = 400
print(dic1)

# li3 = sorted(dic1.items(), key=sort_by_key) # 함수 매개변수 따로 줄 필요 없다
# print(li3)

# 일반 딕셔너리의 내용을 sorted()를 이용하여 정렬을 하면 키를 기준으로 정렬된 리스트가 리턴,
# OrderedDict()로 포장(wrapping)을 하고있다. 기존의 딕셔너리나 리스트의 순서를 지키면서
# 딕셔너리의 형태로 관리 할 수 있음
for k, v in OrderedDict(sorted(dic1.items(), key=sort_by_key)).items():
    print(k,v)