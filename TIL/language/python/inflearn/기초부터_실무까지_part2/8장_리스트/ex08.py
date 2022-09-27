# 리스트 복사하기
# 얕은 복사(shallow copy) : 주소값을 공유하는 개념, 원본 리스트에 영향을 끼친다.
# 진정한 복사는 아니다.

scores = [10,20,30,40,50]
refer = scores
print("socres의 주소값 : ", id(scores))
print("refer의 주소값 : ", id(refer))
# 주소값 변화 없음
refer[0] = 100
refer.append(-70)
refer.insert(1, -100)
print("scores의 주소값 : ", id(scores))
print("refer의 주소값 : ", id(refer))
print("scores의 요소값 : ", scores)
print("refer의 요소값 : ", refer)
