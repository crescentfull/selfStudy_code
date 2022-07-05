# dictionary 딕
# 딕셔너리라는 타입의 형태는 키와 값의 쌍으로 이루어져있다.
# 딕셔너리의 키 값은 유니크한 값이 되어야 한다. 하지만 값은 변경이 가능하다.
# dic = {"name":"song","age":14,"height":160}
# print(dic)
# 딕셔너리가 call by reference가 성립되는 이유는 mutable이기 때문

def change(dic):
    dic["weight"] = 42
    print("change()내의 dic 값 : ", dic)
    print("change()내의 dic 주소값 : ",id(dic))
    
dic = {"name":"song","age":14,"height":160}
print("호출 전 dic의 주소값(id) : ", id(dic))
print("호출 전 dic의 값 : ", dic)
x = change(dic)
print("호출 후 x의 주소값(id) : ", id(x))
print("호출 후 x의 값 : ", x)
print("호출 후 dic의 주소값(id) : ", id(dic))
print("호출 후 dic의 값 : ", dic)
