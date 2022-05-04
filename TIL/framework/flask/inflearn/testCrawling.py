import requests
from bs4 import BeautifulSoup
from firstClass import data_list_minus

res = requests.get('https://davelee-fun.github.io/blog/crawl_html_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
link_titles = soup.select("ul#hobby_course_list > li")
print(link_titles)
data = list()
for link_title in link_titles:
    data.append(link_title.get_text())

data_list_minus(data)
print(data)