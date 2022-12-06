# 텍스트 마이닝 기법 기초
def file_read(text):    
    f_name = open("/Users/yeongroksong/Desktop/study/code/TIL/language/python/inflearn/기초부터_실무까지_part3/12강_collection/law.txt",
                  mode='r', encoding='UTF-8')
    for line in f_name:
        words = line.strip().split()
        for word in words:
            if len(word) >= 2:
                text.append(word)
    print(text)
    
if __name__ == "__main__":
    from collections import defaultdict,OrderedDict
    text = []
    file_read(text)
    word_count = defaultdict(lambda : 0) # 값을 0으로 초기화
    # text에 담긴 단어들의 빈도수를 증가시키는 부분
    for word in text:
        word_count[word] += 1
    
    for i, v in OrderedDict(sorted(word_count.items(), key=lambda t:t[1], reverse=True)).items():
        if v >= 2:
            print(i, v)