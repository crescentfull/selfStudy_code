# 리스트 복사
# deep copy
# 주소값을 공유하는 얕은 복사가 아니라 새로운 리스트 객체를 생성해서 새로운 주소값이
# 할당되어 리스트 객체에는 전혀 영향을 끼치지 않는다.

# 첫번째 방법
scores = [10,20,30,40,50]
refer = list(scores)
print("scores 주소값 : ", id(scores))
print("refer 주소값 : ", id(refer))
refer[0] = 100
refer.append(-500)
refer.insert(2,-123)
print("scores 주소값 : ", id(scores))
print("refer 주소값 : ", id(refer))