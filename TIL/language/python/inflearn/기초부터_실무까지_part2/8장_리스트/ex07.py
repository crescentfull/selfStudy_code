# 리스트 비교 
# 리스트가 일치하려면 반드시 같은 자료형이어야한다.
# 길이가 다르면 false
li1 = [1,2,3]
li2 = [1,2,3]
print(li1==li2)
li1 = [1,2,5]
li2 = [1,2,3]
print(li1==li2)
li1 = [1,2]
li2 = [1,2,3]
print(li1==li2)
li1 = ["dkd",2,3]
li2 = [1,2,3]
print(li1==li2)

# 리스트 > , < 는 ASCII 코드로 비교를 하는 것
li1 = ["a","b","c"]
li2 = ["a","b","g"]
print(li1<li2)
print(li1>li2)

print(ord("a")) # ord() ASCII 코드 숫자 치환해줌
print(chr(100)) # chr() ASCII 코드 숫자를 문자로 치환해준다

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# 정렬하는 방법
# 1번째 : 리스트객체의 sort() 메소드를 이용하는 방법
li = [30, 40, 50, -10, -20]
a = li.sort() #리턴값이 없다. 원래 값을 변경시켜버린다
print(li) 
print(a) #출력 안됨none
#2번쨰 내장함수 sorted()
li = [30, 40, 50, -10, -20]
a = sorted(li)
print(li) 
print(a) #변경된 값이 리턴되어 출력된다.
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# 역순(내림차순)정렬
li = [30, 40, 50, -10, -20]
li.sort(reverse=True)
print(li)

#문자열 정렬
# 유니코드 기준
li = ["가나","다라","다사사","하라","자차"]
liSort = sorted(li, key=str.lower)
print(liSort)

#문자열 분할
# split() 문자열을 분할해서 리스트형태로 반환한다.
statement = "나는 건국대학교 문과대학 선진문과대 등등등 누구인ㅂ니다.안녕하십니까 반가워요."
li = statement.split()
print(li)
li2 = statement.split(".")
print(li2)