# 람다식(무명함수, 익명함수)은 이름이 없는 함수를 만드는 방법을 말한다. 이름은 없고 몸체만 존재하는 함수이다.
# 람다식은 def 키워드를 사용하지 않는다.
# !return 키워드도 사용하지 않는다.

# 람다식을 이용한 간단한 더하기 기능
f = lambda x, y : x + y         # 람다 정의
print(f(10,100))
print("-"*40)

# 함수로 한다면
def sum(x,y):
    return x+y

print(sum(1,100))