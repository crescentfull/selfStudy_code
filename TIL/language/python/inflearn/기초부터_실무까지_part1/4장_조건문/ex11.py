# 문자열의 중앙에 있는 문자를 추출해서 출력을 하는 프로그램을 만들기
# 문자열이 "weekwday"라면 중앙의 문자는 "k"가 된다.
# 하지만, 만약 문자열이 짝수 개의 문자를 가지고 있다면 중앙에 문자를 
# 2개의 문자를 출력한다. 예를 들어서 "monday"라면 "nd"를 출력하도록

str_input = input("문자를 입력하세요. : ")
length = len(str_input) #문자열 길이 구하기
print(length)
midium = length//2
string  = str_input[midium-1]
string2 = str_input[midium]
print(type(string))
if length%2 == 0:
    print("문자값 : ",string,string2)
else:
    print(string2)
