# 회문이란 것은 앞으로 읽으나 뒤로 읽으나 동일한 문장을 의미한다.
# 예를 들면 "mom","civic","dad", "기러기","토마토" 등등
# 사용자로부터 문자열을 입력받고 회문인지 아닌지 프로그램 작성해보자

# 내풀이
def checkWord(word):
    while True:
        if word == word[::-1]:
            return True
        else:
            return False
        
# if __name__ == "__main__":
#     word = input("문자를 입력하세요 : ")
#     checkWord(word)
def main():
    string = input("문자열을 입력하세요 : ")
    string = string.replace(" ","")
    if len(string) <= 1:
        print("한글자는 안됩니다.")
    else:
        if checkWord(string) == True:
            print(string + "은 회문입니다.")
        else:
            print(string + "은 회문이 아닙니다.") 
"""
def check(s):
    # 단어의 처음 인덱스와 마지막 인덱스를 저장하는 코드
    low = 0
    high = len(s)-1
    
    while True:
        # 회문이라면 아래 조건문에 해당할 것이다.
        if low > high:
            return True
        
        s1 = s[low]
        s2 = s[high]
        print(s1, s2)
        
        # 값이 틀릴 경우
        if s1 != s2:
            return False
        # 인덱스를 증가시켜서 서로 비교항목을 바꾸도록 한다.
        low += 1
        high -= 1
"""
if __name__ == "__main__":
    main()
        