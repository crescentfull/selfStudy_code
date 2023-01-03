# 이미지 복사하기
infile = open('sample.png','rb')
outfile = open('sample_copy.png','wb')

while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:         # 파일의 끝이라면
        break
    outfile.write(copy_buffer)      # 복사될 이미지에 읽은 내용을 추가

infile.close()
outfile.close()
print('sample.png를 sample_copy.png로 복사하였습니다.')