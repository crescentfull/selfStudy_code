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