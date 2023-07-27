from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup)
articles = soup.find_all(name="span")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
    
    
article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])