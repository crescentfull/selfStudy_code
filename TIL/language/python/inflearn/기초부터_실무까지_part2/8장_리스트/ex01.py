# 리스트 실습
# 리스트에 정의 : 대량의 데이터를 저장할 수 있는 공간을 만들어야 하고 이 데이터들을 손쉽게 처리하는 형태의 데이터구조

score = []
print("초기화 값 : ", score)

#append() 정수
score.append(30)
print("30추가 : ",score)

#append() 문자열
score.append("ㅇㅇㅇ")
print("ㅇㅇㅇ 추가 : ",score)

#append() 실수
score.append(10.22)
print("10.22추가 : ",score)

print("리스트 크기 : ", len(score))

#리스트값 순회
for i in range(len(score)):
    print (f"score 인덱스 구성 {i}번째 : ",score[i])
#리스트값 순회하여 바꾸기
for i in range(len(score)):
    score[i] = "d"
    print(score)
    
# list 클래스(속성(멤버변수),기능(멤버메서드), 생성자) 이용하여 리스트 만들기
li1 = list() #매개변수가 없는 생성자를 호출(붕어빵을 만드는 형태) 
li2 = list("안녕")
li3 = list(range(0,5,2))

#내장리스트
li1 = [12, 12.777, "안녕"]
print("li1 : ",li1)
print("li1[0] : ", li1[0])
li2 = [["서울",10],["뉴욕",50],["파리",70]]
print("li2 : ",li2)
print(li2[0][0])
print(li2[0][1])

print(li2[1][0])
print(li2[1][1])
