import csv

f = open("files/weather.csv", 'r')
data = csv.reader(f)
header = next(data) # header 제거하기
temp = 1000

for row in data:
    if temp > float(row[3]): # 최저 기온은 3번 인덱스
        temp = float(row[3])

print('가장 추웠던 온도는? : ', temp, '입니다.')
f.close()