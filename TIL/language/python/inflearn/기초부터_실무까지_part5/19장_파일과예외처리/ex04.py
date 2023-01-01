# 파이썬에서 파일을 읽는 방법
# read(), readline(), readlines()
'''
read() : 모든파일의 내용을 읽음
readline() : 한 번에 한 라인씩 읽어들인ㄷ
readlines() : 여러 라인을 리스트에 저장한다. 기본적으로 빈칸(개행 \n)이 포함
'''

# read()로 test.txt 읽기

print('1. read() 함수 읽기')
file = open("test.txt", "r")
string = file.read()
print(string)
file.close()

# readline()로 test.txt 읽기

print('2. readline() 함수 읽기')
file = open("test.txt", "r")
string = file.readline()
print(string)
while string != '':
    print(string)
    string = file.readline().rstrip()
file.close()

# readlines()로 test.txt 읽기

print('3. readlines() 함수 읽기')
file = open("test.txt", "r")
list = file.readlines()
print(type(list))
string = ''.join(list)
print(string)
file.close()