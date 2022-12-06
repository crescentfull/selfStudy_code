# namedtuple 모듈은 튜플의 형태로 데이터를 구조화에 맞게끔
# 저장하는 자료구조이다

# 일반적인 튜플의 경우
person1 = ("송영록", 14, "남")
person2 = ("송주현", 11, "여")

for i in [person1,person2]:
    # %n이 들어가면서 튜플의 값들을 각각에 형식지정자에 맞게 적용
    print("%s은(는) %d세의 %s성입니다." %i)

print("-"*30)
# namedtuple 인 경우
from collections import namedtuple
# person 이라는 namedtuple을 정의
person = namedtuple(typename="person", field_names=('name age gender addr'))
p1 = person(name='김연아', age=32, gender='여', addr='d')
p2 = person(name='손연재', age=28, gender='여', addr='d')
for n in [p1,p2]:
    print("%s은(는) %d세의 %s성입니다. 사는도시 %s" %n)

# person 이라고 정의를 해놓았고 그의 필드들이 3개가 존재하고 있기 때문에 
# namedtuple은 (접근연산자)를 이용할 수도 있다.
print(p1.name, p1.age, p1.gender,p1.addr)
print(p2[0],p2[1],p2[2],p2[3])

print("-"*30)
# namedtuple의 _make() 메소드 : 기존에 생선된 namedtuple에 # 새로운 인스턴스를 생서해주는 메서드
p3 = person._make(['송영록',15,'남','대구'])
print(p3)

for n in [p1,p2,p3]:
    print("%s은(는) %d세의 %s성입니다. 사는도시 %s" %n)

# _replace()
p1 = p1._replace(name='강백호')
p2 = p2._replace(age=44)
p3 = p3._replace(addr='서울')
print("-"*30)

for n in [p1,p2,p3]:
    print("%s은(는) %d세의 %s성입니다. 사는도시 %s" %n)

# _fields
print(p1._fields) # 선언한 변수의 필드명을 tuple형태로 return

# getattr() 은 필드명으로 해당 값을 출력할 때 사용한다
print(getattr(p1, 'name'))

# **(double-star-operator)은 namedtuple() 딕셔너리 형태의 자료구조 namedtuple() 변환하여 반환
dic = {"name" : "신으비", "age" : 15, "gender":"여", "addr":"대전"}
print(dic)
p4 = person(**dic)
print("%s은(는) %d세의 %s성입니다. 사는도시 %s" % (p4.name, p4.age, p4.gender, p4.addr))
print(type(p4))