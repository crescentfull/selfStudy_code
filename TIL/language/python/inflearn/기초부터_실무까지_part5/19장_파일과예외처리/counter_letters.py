# 사용자로부터 파일 안에 문자들의 갯수를 세는 프로그램을 작성하기
filename = input('파일명을 입력하세요 : ').strip()
infile = open(f'files/{filename}', 'r')

freqs = {}
for line in infile:
    for char in line.strip():       # 문자 양쪽 공백제거
        if char in freqs:
            freqs[char] += 1        # 문자 누적
        else:
            freqs[char] = 1         # 제일 처음 나왔을때 1 
print(sorted(freqs.items()))
infile.close()