# Beautiful Soup를 이용한 웹 스크래핑

from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser") #
print(soup.title) # 타이틀 전체
print(soup.title.name) # 타이틀 
print(soup.title.string) # 타이틀 태그 안의 문자열
print(soup)
print(soup.prettify()) # 확인하기 쉽게 해준다.

print(soup.a)
print(soup.li) # 원하는 태그를 불러올수 있다.