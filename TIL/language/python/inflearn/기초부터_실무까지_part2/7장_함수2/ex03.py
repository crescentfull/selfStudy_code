# call by reference 실습
# 함수를 호출할 때, 실질적인 주소값이 넘어가서 호출한 곳에 영향을 끼치는 형태
# 파이썬에서는 함수의 매개변수 값이 전부 객체인데 list, dictionary와 같은 
# mutable object 즉 변경 가능한 객체이므로 call by objective-reference 라고 한다.

def change(li):
    print("change()함수 내의 연산 전 li값 : ",li)
    print("change()함수 내의 연산 전 li의 주소값 : ", id(li))
    li += [100,200]
    print("change()함수 내의 연산 후 li값 : ",li)
    print("change()함수 내의 연산 후 li의 주소값 : ", id(li))

list = [1,2,3,'dd']
print("change()함수 호출 전 list의 주소값 : ", id(list))
change(list)
print("change()함수 호출 후 list의 주소값 : ", id(list))