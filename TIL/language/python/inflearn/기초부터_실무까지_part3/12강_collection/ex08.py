# 함수를 이용하여 각 알파벳의 글자 수를 세어서 key로 저장을 하고
# 단어는 값으로 딕셔너리를 리턴하는 코드를 보자( *set을 이용)

from collections import defaultdict

# words 라는 리스트를 받아서 길이를 키로 하고 값을 리스트 값으로 하는 딕셔너리 리턴하는 함수

def counterWords(words):
    grouper = defaultdict(set)
    print(grouper)
    for word in words:
        # word의 길이를 구하여 그 길이를 키로하고 word의 내용을 값으로 하고 있다.
        length = len(word)
        grouper[length].add(word)
    return grouper
    
    

if __name__ == "__main__":
    set1 = set()
    set1.add("한국")
    set1.add("일본")
    set1.add("대만")
    set1.add("중국")
    set1.add("인도")
    dic1 = counterWords(set1)
    print(dic1)