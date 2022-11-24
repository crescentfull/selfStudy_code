# 문제
# 머리글자어(acronym)은 NATO(North Atlantic Treaty Organization)
# 각 단어의 글자어를 모아서 만든 문자열, 사용자로부터 문장을 입력하면 해당되는 머리
# 글자어를 출력하는 프로그램
'''
출력결과
문자열을 입력하시오 : North Atlantic Treaty Organization
>>> ACRONYM : NATO
'''

def main():
    string = 'North Atlantic Treaty Organization'
    ACRONYM = ""
    # for i in string:
    #     if i.isupper():
    #         ACRONYM += i
    for word in string.upper().split():
        ACRONYM += word[0]
        
    print("ACRONYM : ",ACRONYM)
    
if __name__ == '__main__':
    main()