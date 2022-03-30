#문자열 실습
#큰따옴표(double quotation)
welcome = "Happy New Year 2021"
print(welcome)  
#작은따옴표(single quotation)로 묶어도 문자열이 된다.
welcome = 'Happy New Year 2021'
print(welcome)

# "" 안에 ''를 이용하면 출력가능하다
# 반대도 가능 반대추천 // 왜? print('')에서 쌍따옴표 사용 안됨,,
message = "a가 '안녕'이라고 말한다"
message2 = 'aaaa "d"ffff '
print(message)
print(message2)

# 파이썬에서는 따옴표를 출력하고자 할 때,\를 이용
## \가 따옴표를 앞에 있으면 '는 특수한 의미를 잃어버리고 하나의 문자로 편승이 되어 문자열을 이룬다.
message = 'doesn\'t'
print(message)

#개행문자 \n
message = "first\nSecond\nThird"
print('*****개행문자*****')
print(message)

#\t는 글자를 띄워준다
print("ddfsdfsdfsd\tdsfsfsddsfs")

#문자열의 길이(영어나 한글 상관 없음)를 알고자 한다면 len()함수를 이용한다.
message = "world"
print("문자열의 길이 : ", len(message))
