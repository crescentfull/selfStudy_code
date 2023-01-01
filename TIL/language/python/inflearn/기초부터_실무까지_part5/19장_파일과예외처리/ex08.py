# csv 파일 읽기

import csv
f = open('files/weather.csv','r')
data = csv.reader(f)        # csv 파일은 reader() 함수를 사용해야한다
# 헤더 제거
header = next(data)

for row in data:
    print(row)
f.close()