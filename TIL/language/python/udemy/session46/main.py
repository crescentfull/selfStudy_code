import requests
from bs4 import BeautifulSoup

# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://comic.naver.com/webtoon"

response = requests.get(URL)
response.raise_for_status()
website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, "lxml")

all_movies = soup.find_all("ul", attrs={"class":"AsideList__content_list--FXDvm"})
print(all_movies)

movie_titles = [movie.getText() for movie in all_movies]
print(movie_titles)

# 안한다.
# 제대로된 크롤링도 아니고 api 끌어다가 쓰는건데 정수를 배워보겠다