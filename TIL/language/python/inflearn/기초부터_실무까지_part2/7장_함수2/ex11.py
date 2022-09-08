# 여러개의 값을 반환하는 함수 
# 타 프로그래밍 언어에서는 함수가 항상 하나의 값만을 반환하거나 반환값이 없다.
# 그러나 파이썬에서는 튜플을 이용햐여 여러개의 값을 반환 할 수 있다.

#튜플(tuple)은 리스트와 흡사하나 몇가지 다른 부분이 존재한다.

# 리스트 [] 튜플 ()
# 리스트는 변경가능 객체(생성,삭제,수정,삽입), 튜플은 변경 불가능

def tuple_return():
    return 1, "안녕", 5

a, b, c = tuple_return()
tuple_variable = tuple_return()
print(a,b,c)
print(tuple_variable)
print(type(tuple_variable))