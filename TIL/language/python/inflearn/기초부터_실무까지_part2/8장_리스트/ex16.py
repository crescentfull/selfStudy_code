# 기본적인 파일 입출력 실습

data = []
filePoint = open("/Users/yeongroksong/Desktop/안녕.txt", mode="r", encoding="UTF-8") # mode = "r" read
# print(type(filePoint))
# readlines() 파일에 저장된 내용을 한번에 다 읽는다.
# for line in filePoint.readlines():
#     print(line.strip()) # strip() 문자열 양쪽 공백 제거하는 함수. 파일을 읽어들일 때는 엔터키도 제거해줌
# 프로그램 리소스를 다 사용 했으면 반드시 close() 메서드를 호출하도록 한다..
print("파일 읽기")
for line in filePoint.readlines():
    data.append(line.strip())

print(data)
filePoint.close()

## 파일 내용 쓰기
filePoint = open("/Users/yeongroksong/Desktop/안녕.txt", mode="w", encoding="UTF-8") #파일의 mode가 w인 경우에는 덮어써진다.
print("파일 쓰기")
filePoint.write("dd")
filePoint.write("dfsfsdf")
filePoint.close()

## 내용 추가
filePoint = open("/Users/yeongroksong/Desktop/안녕.txt", mode="a", encoding="UTF-8") # mode = "a" append
print("파일 내용 추가")
filePoint.write("1.gdkjgslghl")
filePoint.write("2.23232")
filePoint.close()

# CSV 파일 읽기
import csv

fp = open("/Users/yeongroksong/Desktop/test.csv", mode="r")
reader = csv.reader(fp)
for data in reader:
    print(data)
fp.close()