# 함수를 이용하여 딕셔너리를 초기화하는 코드를 실습하기

from collections import defaultdict
# 일반 딕셔너리 초기화 방법
def countLetters(word):
    counter = {}
    for letter in word:
        # 넘어온 문자열의 값을 하나가 키가 되고 그 키의 기본값으로 0을 설정함.
        if letter not in counter:
            counter[letter] = 0
    return counter

# setdefault() method
def countLetters_setdefault(word):
    counter = {}
    for letter in word:
        # 위의 countLetters() 보다 조건절은 사라졌지만 루프를 돌때마다, setdefault() 를 계속 호출하므로 약간 비효율적
        counter.setdefault(letter, 0)
    return counter

# defaultdict 모듈을 직접 이용하는 방법
# defaultdict()
def countLetters_defaultdict(word):
    counter = defaultdict(lambda : 0)
    for letter in word:
        counter[letter] += 1
    return counter

if __name__ == "__main__":
    dic = countLetters("가나다라마")
    print()
    print(dic.items())

    print("----------------------------------")
    
    dic = countLetters_setdefault("가나다라마")
    print(dic.items())
    
    print("----------------------------------")
    
    dic = countLetters_defaultdict("가나다라마")
    print(dic.items())

# 함수를 이용해서 알파벳의 글자 수를 count해서 저장하고
# 딕셔너리를 리턴하는 코드를 보자