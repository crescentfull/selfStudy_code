# 반복문으로 문자열 처리하기 연습
string = "fruit"
for _ in string:
    print(_)
#사용자로부터 문자열(영어)을 입력 받아서 모음을 전부 없애는 코드
print("**********************************")
string = input("문자열을 입력하세요(영문자) : ")
# 영문자 모음의 문자열
vowels = "aeiouAEIOU"
res = ''.join( x for x in string if x not in vowels)
print("최종 결과 : ", res)

print("**********************************")
result = ""
for letter in string:
    #하나씩 반복하는 문자가 모음 문자열에 존재하지 않는다면 참을 반환
    if letter not in vowels:
        result += letter
print("출력 : ",result)

#문자열 입력받아서 자음과 모음의 갯수를 출력하는 프로그램을 작성
print("**********************************")
origin = input("문자열을 입력하시오 : ")
word = origin.lower() #입력받은 문자 소문자로 변경
