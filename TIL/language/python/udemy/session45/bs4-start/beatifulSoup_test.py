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

all_anchor_tags = soup.find_all(name="a") # 모든 a 태그
print(all_anchor_tags)

# for문 이용
for tag in all_anchor_tags:
    tag.getText() # a태그의 text만 출력

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

h3_heading = soup.find_all("h3", class_= "heading")
print(h3_heading)

# company_url = soup.select_one(selector="p a") # CSS selector

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)

