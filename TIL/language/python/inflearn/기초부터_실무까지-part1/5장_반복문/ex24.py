# 입력받은 문자열의 모든 공백을 제거한 문자열을 출력하는 프로그램을 만드시오

string = input("문자열 입력 : ")

res = string.replace(" ","")

print(res)

new_string = ""
for i in string:
    if i != ' ':
        new_string += i
print(new_string)