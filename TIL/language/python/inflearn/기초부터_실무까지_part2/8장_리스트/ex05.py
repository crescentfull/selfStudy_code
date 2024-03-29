# 인덱싱 : 리스트에서 하나의 요소를 인덱스를 통하여 참조하는 것
from operator import index
from xml.dom.minidom import Element


li = ["안녕", "송영록", 10, 100, -11]
print(li)
# 음수 인덱스는 뒤에서부터 계산한다. 시작값은 -1
print(li[-2])
print(li[-2 + len(li)])

# 슬라이싱을 시작할때 앞의 인덱스가 없으면 0부터 시작하는것
print(li[:2])
print(li[:-1])

# 요소 추가
# append insert
listTest = ["TV","AUDIO","COMPUTER"]
listTest.append("마우스")
print("APPEND : ",listTest)
listTest.insert(1,"휴대폰")
print("INSERT : ",listTest)

# 요소찾기
# if _ in [리스트]/not in [리스트]
listTest2 = ["아이언맨","슈퍼맨","배트맨"]
if "배트맨" in listTest2:
    print("okok")

if "조커" not in listTest2:
    print("ok!ok!")
    
# 요소 위치찾기 index()
print(listTest2.index("아이언맨"))
print(listTest2.index("슈퍼맨"))
print(listTest2.index("배트맨"))

# 요소삭제
# pop(인덱스)
# remove("요소")
# del {리스트명}[{인덱스}]
hero = ["아이언맨","슈퍼맨","배트맨","헐크","토르","베놈"]
print("element : ", hero)
hero.pop()
print("element : ", hero)
hero.pop(0)
print("element : ", hero)
# remove()메서드는 리스트의 요소 중 인덱스가 빠른순서로 제거한다.
# 한번에 제거 하고 싶으면 반복문을 이용해서 제거
hero = ["배트맨","아이언맨","슈퍼맨","배트맨","헐크","토르","베놈"]
value = ["배트맨"]
while value in hero:
    hero.remove(value)
print(hero)
#? 뭐지 왜 삭제가 안돼
hero.clear()
print(hero)