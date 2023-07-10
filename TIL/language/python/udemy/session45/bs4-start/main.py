# Beautiful Soup를 이용한 웹 스크래핑

from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, )