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
    
# 딕셔너리 동등성 비교
# 동등성은 논리적 동등이라는 것을 의미한다. 논리적 동등이란 주소는 다르지만 요소들의 값이 순서가 비록 틀리더라도 논리적 동등으로 바라보는 시점
str1 = "신은혁"
str2 = str()
str2 = "신은혁"
print(id(str1))
print(id(str2))

print("------------------------------")
dic1 = {"가":1,"나":2,"다":3}
dic2 = {"가":1,"다":3,"나":2}
print(dic1)
print(dic2)
print(dic1 == dic2)
print("------------------------------")
from collections import OrderedDict
ordered_dic1 = OrderedDict({"가":1,"나":2,"다":3})
ordered_dic2 = OrderedDict({"가":1,"다":3,"나":2})
ordered_dic3 = OrderedDict({"가":1,"나":2,"다":3})
print(id(ordered_dic1))
print(id(ordered_dic2))
print(ordered_dic1 == ordered_dic2)
print(ordered_dic1 == ordered_dic3)
# 결론
# OrderedDict 모듈은 딕셔너리의 순서대로 저장하지 않는 방식을 순서대로
# 저장하는 방식으로 개선되었다. (파이썬 버전 3.6 이후로는 저장과 출력이 OrderedDict와 동일하게 작동을 하고 있지만. 2.x 버전에서는 문제점이 있디)
# 딕셔너리의 동등성 비교에서 일반적인 딕셔너리는 순서를 유지하지 않아도 해당 키와 값이 동등하다면 True를 리턴하지만, OrderedDict 에서는 순서, 키와 값이 무조건 같아야 True를 리턴하는 좀 더 향상된 동등성 비교로 개선
# OrderedDictfmf 사용 하면 정확한 데이터의 순서나 값을 유지하는데 일반 딕셔너리에 비해서는 좋으면이 존재
# 웬만하면 딕셔너리보다는 OrderedDict을 쓰는건 어떤가?