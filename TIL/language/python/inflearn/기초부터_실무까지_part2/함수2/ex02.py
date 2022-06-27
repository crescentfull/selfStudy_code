#문자열 실습

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