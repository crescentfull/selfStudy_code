#문자열 실습
#문자열에 대한 내용도 숫자형의 객체와 동일한 iㅡmutable object이다
# 파이썬의 경우는 타 언어의 call by reference(value)의 개념과는 조금 다르다
# 그 이유는 파이썬은 모든 것을 '객체'롤 판단하기 때문
def change(string):
    string += '공부하자'
    print("change()내의 string 값 : ", string)
    print("change()내의 string 주소값 : ",id(string))
    
msg = "안녕하세요. 저는 파이썬을"
print("호출 전 n의 주소값(id) : ", id(msg))
print("호출 전 n의 값 : ", msg)
x = change(msg)
print("호출 후 x의 주소값(id) : ", id(x))
print("호출 후 x의 값 : ", x)
print("호출 후 n의 주소값(id) : ", id(msg))
print("호출 후 n의 값 : ", msg)