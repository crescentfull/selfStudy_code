# 내장함수에 대한 실습
# abs() : 절댓값을 반환
i = -20
print('i의 절댓값 : ', abs(i))
i = -20.55
print(abs(i))
print("-"*40)

# all() : 시퀀스(리스트, 딕셔너리 등)를 받아서 시퀀스의 모든 항목이 참이면 True 반환한다.
# and 조건과 유사하다. 하나라도 0인 값이 들어가면 False 리턴한다.
list2 = [1, 4, 7, 10] # 모든것이 참
print(all(list2)) 
list2 = [0, 1]
print(all(list2))

print("-"*40)

# any()함수 : 시퀀스 객체에 있는 한개의 항목이라도 참인 경우에 참을 반환한다.
# or 개념과 유사하다
list2 = [0, 7, 10, 20]       # 1개의 값이 False 이므로 True 리턴
print(any(list2))
list2 = [0, 0, 0, 0]         # 모든 값이 False 이므로 False 리턴
print(any(list2))

print("-"*40)

# bin() : 10진수를 이진수로 표현해주는 함수, 항상 접두사 0b로 시작한다.
y = bin(15)
print(y)
print("-"*40)

#eval() : 전달된 수식을 구문 분석을 하고 프로그램 내에서 수식의 값을 계산
exp = input("수식을 입력하세요 : ")
print(eval(exp))
# 전역변수도 가능
x = 10
y = 10
print(eval("x*y"))
print("-"*40)

print(sum([1,10,100]))

print("-"*40)
# len() : 객체의 길이를 반환하는 함수, 문자열의 길이를 계산하는데 유용하다.
# 리스트에 len() 사용하게 되면 리스트 안에 있는 항목의 갯수를 리턴
# 딕셔너리, 튜플에서도 항목의 갯수를 반환

# list() 리스트 생성

# map() : 반복가능한 객체(리스트, 튜플 등)의  각 항목에 주어진 함수를 적용한 후 적용 결과를 반환한다.
# 적용시킬 함수 작성
def square(n) :
    return n*n
list3 = [1,2,3,4,5]
res = list(map(square, list3)) # list3에 있는 하나하나의 값에 sqare 함수를 적용시키고 있다.
print(res)
print("-"*40)

# dir() : 객체가 가지고 있는 변수나 함수를 보여준다. 리스트로 결과를 반환한다.
print(dir([1,2,3]))

# max(), min() : 리스트나 튜플, 문자열에서 가장 큰 항목과 작은 항목은 반환한다. 정수에서 가장 큰 값과 작은 값을 리턴

print("-"*40)
# enurmerate() : 시퀀스 객체를 입력받아서 열거형 객체를 반환, 열거형 객체는 첫 번째 요소로는 번호, 두번째 값은 번호에 해당하는 값을 갖는 객체이다. 열거형이란 한정된 값을 가지고 가독성을 높이고 문서화를 하는데 도움을 주는 타입이 바로 열거형이다.
seasons = ["봄", "여름", "가을", "겨울"]
print(list(enumerate(seasons)))
# enumerate()는 start라는 매개변수가 값을 지정하지 않는다면 0부터 시작한다.
# 스타트값을 이용하면 우리가 원하는 값으로 기준값을 설정할 수가 있다.
print(list(enumerate(seasons, start=1)))
print("-"*40)

# filter() : 조건을 제시하는 함수를 만들어서 그 조건에 해당하는 요소를 추출하고자 할 때 사용
# 리턴값들은 리스트의 형태로 반환된다
# 조건을 제시해주는 함수 정의
def myfilter(x):
    return x>3

result3 = filter(myfilter, (1,2,3,4,5,6,7))
print("3을 초과한 수 : ", list(result3))

print("-"*40)
# zip() : 2개의 리스트를 하나로 묶어주는 함수
# 요소의 갯수를 맞추어 주는 것이 데이터 누락에 도움이 된다.
numbers = [1,2,3,4]
list4 = ["하나","둘","셋","넷"]
print(list(zip(numbers, list4)))

# for문을 이용한 방법
names = ["신은혁","김연아","손연재"]
scores = [100,99,88]
for x,y in zip(names, scores):
    print(x, y)