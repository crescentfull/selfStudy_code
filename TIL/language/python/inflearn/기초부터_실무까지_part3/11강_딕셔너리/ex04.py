# 사용자가 지정하는 파일을 읽어서 저장되어진 각각의 단어가 몇번이나
# 나오는지 계산하는 프로그램을 작성하여 보자
# 출력결과
# 파일 이름 입력 : words.txt
#  {asia':3, 'do':2,'신은혁':2}

# 파일 이름 입력 받기
f_name = input("파일 이름 입력 : ")
file = open(file=f_name, mode="r", encoding="UTF-8")

word_count = dict()     # 빈 딕셔너리 생성
for line in file:        # 파일로부터 한줄씩 읽음
    words = line.split()            # 읽어온 한줄의 문장을 단어(토큰)로 나눔
    for word in words:              # 단어 리스트에서 해당하는 단어만큼 루프를 돔
        if word not in word_count:      #단어가 단어리스트에 존재하지 아니하면...
            word_count[word] = 1
        else:
            word_count[word] += 1       #존재한다면 값 증가
            
print(word_count)
file.close()