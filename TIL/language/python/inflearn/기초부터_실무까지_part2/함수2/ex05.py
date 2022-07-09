# 전역변수를 함수안에서 값을 변경하고자 한다면 
# global 키워드를 사용하여야 한다.

def test():
    global text #test() 함수안에서 전역변수인 text를 사용하겠다는 것을 인터프리터에게 알려줌
    print("함수 내 1 : ",text)
    text = "파이썬" #전역변수 값 변경
    print("함수 내 2: ",text)

text = "자바"
print("1 : ",text) #전역변수 변경전 
test()
print("2 : ",text) #전역변수 변경후