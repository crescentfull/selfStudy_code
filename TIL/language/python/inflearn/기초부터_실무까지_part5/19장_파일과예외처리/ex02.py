# 파일 쓰기 write
file = open('/Users/yeongroksong/Desktop/test.txt','w')
file.write('dd\n')
file.close()
# 텍스트 파일에 내용 추가
file = open('/Users/yeongroksong/Desktop/test.txt','a')
file.write('aa')
print("송영록\n", file=file) # 이것도 됨
file.close()