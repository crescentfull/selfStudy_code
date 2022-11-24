# str 클래스 메서드 실습
# split() : 문자열에서 단어(토큰)을 분리하고자 할 때 사용하는 메서드이다.
# 인자값으로 구분자(seperator)를 주게 되면 주어진 구분자로 문자열을 구분한다.
# 기본 인자값은 공백
string = "안녕 john 난 지금 학교를 가고 있어"
li1 = string.split()
print(li1)
print(type(li1))

string = "안녕,john,난,지금,학교를,가고,있어"
li2 = string.split(",")
print(li2)

import regex

string = "안녕/john/난|지금|학교를:가고|있어"
li3 = regex.split("[/:|]", string) # 콤마로 분리
print(li3)

# 문자열 검사
string = "abcd"
print(string.isalpha()) # 문자열이 영문자인지 확인하는 코드
string = "1234"
print(string.isdigit()) # 문자열이 10진수인지
print(string.isdecimal())
string = "abcd1234"
print(string.isalnum()) # 문자열이 영문자, 숫자인지 확인
string = "   "
print(string.isspace()) # 문자열이 공백인지

print("---------------------부분 문자열----------------")
# 부분 문자열 검색 실습
string = "32.py"#input("파이썬 소스 입력 : ")
# endswith({문자열}) 메소드는 인자값 문자열로 끝이나면 True를 리턴한다.
if string.endswith(".py"): 
    print("올바른 파일이름 입니다.")
else:
    print("틀린 파일 이름입니다.")
    
print("-------------------------------")
string = "2021-03-04.txt"
if string.startswith("2021"):
    print("2021년 파일 ok")
else:
    print("2021년 파일이 아니다")
    
print("----------------------------------")
string1 = "asbcd"
print(string1.upper())
string = "ABDEDD"
print(string1.lower())
print(string1.capitalize()) # 앞 한 글자만 대문자로 변경
print(string1.title())      # 앞 한 글자만 대문자로 변경

print("--------------------------------")
# format()은 포맷 {} 을 만들어 놓고 문자열을 생성하는데 사용하는 것
string = "{}b{}"
print(string.format("a","c"))

print("------------------------------")
# join()은 리스트 같은 반복(iterable) 인자를 전달받아서 문자열로 연결하는데 사용
string = ["a","b","가"]
print("!".join(string))

print("---------------------------------")
# 전달받은 인자값으로 문자열을 나눈다. 리턴 타입은 튜플이다.
string = "song972@konkuk.ac.kr"
print(string.partition("@"))

print("---------------------------------")
# count()는 인자값으로 들어오는 값을 문자열에서 몇 개 있는지 카운팅을 해준다.
# 찾는 인자값이 없다면 0을 리턴해준다.
string = "aaaaaabcc"
print(string.count("a"))

print("---------------------------------")
# find()메서드는 특정 단어를 찾아서 인덱스를 리턴하고 없다면 -1을 리턴한다.
# index() 차이점
string = "apple"
print(string.find("z"))
# print(string.index("z")) # index()는 특정 단어를 찾으면 리턴하지만 없다면 예외를 발생 시켜버린다.>>> valueError

print("---------------------------------")
# 문자열에서 공백을 제거하는 방법
# strip() : 양쪽 공백 제거, 탭문자, 줄바꿈(enter)도 제거
# lstrip() : 왼쪽 공백만 제거
# rstrip() : 오른쪽 공백만 제거
# 단 메소드로 문자열 중간에 존재하는 공백은 제거할 방법이 없다. (함수를 만들어서 직접 사용해야 한다.)
string = '\t   aaaaaa bbbbbb cccc dddddd       \t'
print(string.strip())
print(string.rstrip())
print(string.lstrip())