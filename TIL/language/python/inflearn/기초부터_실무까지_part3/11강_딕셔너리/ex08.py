# 문제
# 문자열 안에 있는 문자의 개수, 숫자의 갯수, 공백의 갯수를 계산하는 프로그램

"""
출력 결과
문자열을 입력 : A picture is worth a thousand words.
{'digits' : 0, 'spaces' : 6, 'alpahs' : 29}
"""

'''
string = 'A picture is worth a thousand words.'
li = list(string)
print(li)
alpahs = 0
digits = 0
spaces = 0
for i in li:
    if i.isalpha():
        alpahs += 1
    elif i.isdigit():
        digits += 1
    elif i == ' ':
        spaces += 1
print(alpahs)
print(digits)
print(spaces)

res = {}
res['digits'] = digits
res['spaces'] = spaces
res['alpahs'] = alpahs
print(res)
'''

def main():
    string = 'A picture is worth a thousand words.'
    res = {'digits':0,'spaces':0,'alphas':0}
    for i in string:
        if i.isalpha():
            res['alphas'] += 1
        if i.isdigit():
            res['digits'] += 1
        if i.isspace():
            res['spaces'] += 1
    print(res)

if __name__ == "__main__":
    main()