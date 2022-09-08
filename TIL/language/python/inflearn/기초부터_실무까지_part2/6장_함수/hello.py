# 간단한 함수
# def 키워드 
'''
def 함수이름(매개변수)
'''
def say_hello_name(name):  # 함수 선언부(헤더)
    print("hi "+name) # 함수 구현부(=정의부, 바디)
    
# 매개변수 2개
def say_hello_msg(name,msg): # !파이썬에서는 오버로딩의 개념이 없다. 그러므로 이름이 같은 함수라면 마지막에 정의된 함수를 인식하게 된다. 그러므로 필요한 함수라면 꼭 unique한 값으로 하길
    print("hi",name,",",msg)
    print(f"hi {name}, {msg}") # 이게 더 좋아 보인다.

# 값을 반환하는 함수
def get_sum(start,end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    print(f"{start}에서 {end}까지의 누적합계 : ",sum)