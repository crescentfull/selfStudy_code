# 파일은 데이터를 영구적으로 저장하는 형태이다
# 파일을 다루는 방법에 대해서 알아보자
# 1. 파일열기

file = open("/Users/yeongroksong/Desktop/test.txt", mode='r')

line = file.readline().rstrip()
while line != '':
    print(line)
    line = file.readline().rstrip() # rstrip()은 오른쪽에 공백을 제거하는 함수, \n , \t 등을 다 제거해준다.
file.close()