# 리스트 컴프리헨션 문자열
li = ["서울","부산","대구","대전","광주"]
str = [x[0] for x in li] # 첫글자 따기
print(str)
str_last = [x[-1] for x in li]
print(str_last)
length_li = [len(x) for x in li]
print(length_li)

# 상호곱
colors = ["red","yellow","blue","green","purple"]
cars = ["그랜져","소나타","스파크","아반떼","스타렉스"]
cross_multi = [x+":"+y for x in colors for y in cars]
print(cross_multi)