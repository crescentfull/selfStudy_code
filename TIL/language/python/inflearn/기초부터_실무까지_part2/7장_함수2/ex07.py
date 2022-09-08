def test():
    global text # test()함수 안에서 전역변수인 text를 사용하겠다라는 것을 인터프리터에게 알린다.
    print('함수 안 global text : ',text)
    text = '파이썬 공부' # 전역변수 값 -> 지역변수로 변경
    print('함수 안 지역변수 text : ',text)
    
text = '자바 공부'
print('함수 밖 text 함수 실행 전 : ',text) # 함수 실행 전
test()
print('함수 밖 text 함수 실행 후 : ',text) # 함수 실행 후