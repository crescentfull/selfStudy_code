# 함수를 이용하여 딕셔너리를 초기화하는 코드를 실습하기
# 일반 딕셔너리 초기화 방법
def countLetters(word):
    counter = {}
    for letter in word:
        # 넘어온 문자열의 값을 하나가 키가 되고 그 키의 기본값으로 0을 설정함.
        if letter not in counter:
            counter[letter] = 0
    return counter

if __name__ == "__main__":
    dic = countLetters("가나다라마")
    print(dic.items())