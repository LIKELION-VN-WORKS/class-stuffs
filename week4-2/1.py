import requests
from bs4 import BeautifulSoup

url = input("Search the page you want (ex: www.xxx.com): ")

response = requests.get('https://' + url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))