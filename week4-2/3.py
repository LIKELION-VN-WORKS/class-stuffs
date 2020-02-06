import requests
from bs4 import BeautifulSoup

response = requests.get('https://spotifycharts.com/regional')
html = response.content
soup = BeautifulSoup(html, 'html.parser')

list_song = soup.find_all(name = 'td', attrs = {'class': 'chart-table-track'})
list_artist = soup.find_all(name = 'td', attrs = {'class': 'chart-table-track'})

# songs
for index in range(len(list_song)):
    title = list_song[index].find('strong').text
    print(index+1, ':', title)
    if index == 99:
        break

# artists
for index in range(len(list_song)):
    title = list_song[index].find('span').text
    print(index+1, ':', title)
    if index == 99:
        break



