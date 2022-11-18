# 자료구조 :  데이터의 특징을 고려하여 데이터를 저장하는 방법
# 자료구조의 특징 : 최대한 메모리를 효율적으로 저장 및 반환하는 방법으로, 데이터를 관리하는 것
# 대용량일수록 빨리 검색하고, 메모리를 최대한 효율적으로 사용하면서 유저들에게 실행결과를 빠르게 반환 시켜주는 방법

# 스택(stack) : 택시기사님의 동전통, LIFO(Last In First Out)
# 데이터를 저장하는 것을 push, 데이터를 추출할 때 pop이라고 한다.
stack_data = []
stack_data.append(10)
stack_data.append(20)
stack_data.append(30)
stack_data.append(40)
stack_data.append(50)
stack_data.append(60)
print(stack_data)
# 스택에서 추출할 때는 pop()
print(stack_data.pop())
# pop() 메서드는 스택에서 마지막으로 들어온 데이터를 삭제하면서 반환
print(stack_data)

# 입력 텍스트를 역순으로 추출
word = input("문자열을 입력 : ")
word_list = list(word)
print(word_list)

# _ 라는 기호는 파이썬에서 많이 사용되는 기호, for 문을 루핑 시킬때, 루프변수에 값을 사용하지 않을때!
# _ 로 할당 받는 것이다..!
res = []
for _ in range(len(word_list)):
    #res += word_list.pop()
    res.append(word_list.pop())
print(res)