# 하나의 파일을 읽어서 그 안에 알파벳이 몇 개가 있는지 확인하는 프로그램
counter = [0]*26
infile = open('files/mobydick.txt')
ch = infile.read(1)
while ch != "":
    ch = ch.upper() # 대문자로 바꾼다
    if ch >= 'A' and ch <= 'Z': # 알파벳이라면 
        i = ord(ch) - ord('A') # ord()는 유니코드를 반환, A를 빼면 현재 알파벳의 문자번호를 알 수가 있다.
        counter[i] += 1
    ch = infile.read(1)
print(counter)