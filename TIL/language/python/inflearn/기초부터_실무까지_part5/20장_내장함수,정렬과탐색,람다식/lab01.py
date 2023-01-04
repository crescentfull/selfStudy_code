# 내장 함수를 이용한 문제해결
# 초대받은사람
names = ["송영록", "김연아", "손연재", "dd"  ]
# 동행인원
persons = [1, 3, 0, 6]

# 파티의 총 인원을 구하기
print("파티의 총 인원 : ", sum(persons)+4)

# 파티에 한 사람이라도 오는가?
print(any(persons))
# 파티에 동행이 없는 사람이 있나?
print(all(persons))

# 동행인원 묶어서 출력
for x,y in zip(names, persons):
    print(x,y)