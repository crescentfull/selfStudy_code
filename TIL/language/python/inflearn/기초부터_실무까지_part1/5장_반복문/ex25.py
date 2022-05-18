# 입력 받은 문자열을 거꾸로 출력하는 프로그램을 작성하시오
string = input("문자열 입력 : ")
print(string[::-1])

print("************************")
re_string = ""
for i in string:
    re_string = i + re_string # re_string 더하는 위치 중요
print(re_string)
print("************************")
list_string = list(string)
print(list_string)
list_string.reverse() # list 타입에서 제공하는 함수
print(list_string)
print("".join(list_string))
print("************************")
s = reversed(string) # 파이썬 내장함수, 객체로 반환
print(''.join(s))

