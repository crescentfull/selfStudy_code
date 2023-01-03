# 디렉토리에 관련된 실습
import os

# 현재 작업 디렉토리를 얻는 방법
dir = os.getcwd()
print(dir)

print("-"*40)
# 작업 디렉토리 안에 파일들의 리스트를 얻고자 할 때
for filename in os.listdir():
    print(filename)

print('-'*40)
# 파일만 추출하고자 할때...
for filename in os.listdir():
    if os.path.isfile(filename): # file만 추출하고 싶을때! isfile()
        print(filename, '파일입니다.')

print('-'*40)
# 확장자
files = os.listdir()
for name in files:
    if os.path.isfile(name):
        if name.endswith('.png'):
            print(name)
