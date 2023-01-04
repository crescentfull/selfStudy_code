import re

# file = open("files/uscons.txt","r")
# for line in file:
#     line = line.rstrip()        # 오른쪽 공백 없애기
#     if re.search('^[0-9]+', line):
#         print(line)

text = '''
    101 COM Python Program
    102 MAT LinearAlgebra
    103 ENG
'''

# findall() 파일이나 문자열에서 찾고자 하는 것을 모두 찾는다
s = re.findall('\d+', text)     # 숫자 1번 이상 반복하는 정규표현식
print(s)