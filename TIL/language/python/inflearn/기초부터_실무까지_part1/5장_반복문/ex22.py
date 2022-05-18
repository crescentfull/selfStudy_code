# 사용자로부터 문자열을 입력받아서 알파벳 문자, 숫자, 공백(스페이스)의 갯수를 출력

string   = input("문자열을 입력하시오 : ")
alphabet = 0
num      = 0
blank    = 0

for x in string:
    if x.isalpha():
        alphabet += 1
    elif x.isdigit():
        num += 1
    elif x.isspace():
        blank += 1
        
print("알파벳 : ", alphabet)
print("숫자 : ", num)
print("공백 : ", blank)

        