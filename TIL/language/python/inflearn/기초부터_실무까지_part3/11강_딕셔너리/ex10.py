# csv 파일 데이터 파싱

def main():
    f_name = open(file="/Users/yeongroksong/Desktop/study/code/TIL/language/python/inflearn/기초부터_실무까지_part3/11강_딕셔너리/sample.csv", mode="r", encoding="utf-8")
    # read()    : 파일을 처음부터 끝까지 읽을 때 사용
    # readline(): 파일의 내용을 한 줄씩 읽어 들일때 사용
    # readlines(): 파일을 읽으면 한 줄, 한 줄이 각각 리스트의 원소로 들어감
    print(f_name)
    for line in f_name.readlines():
        line = line.strip()
        print(line)

    
    f_name.close()

if __name__ == "__main__":
    main()