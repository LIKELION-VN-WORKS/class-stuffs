import requests
from bs4 import BeautifulSoup

URL = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
query = input("찾고 싶은 뉴스 키워드: ")

fullURL = URL + query
data = requests.get(fullURL).text
soup = BeautifulSoup(data, 'html.parser')
news_title = soup.find_all(class_ = '_sp_each_title') # class_ :  네이버 측에서 방지해 둔 것.

title_array = []
for title in news_title:
    title_array.append(title.get('title'))

print(title_array)