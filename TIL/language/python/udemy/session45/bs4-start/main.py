from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup)
article_tag = soup.find(name="span", class_="titleline")
print(article_tag)
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()
print(article_text)
print(article_link)