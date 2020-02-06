import requests
import webbrowser

search = '멋쟁이 사자처럼'
queryString = {'q' : search}
searchEngine = 'https://www.google.com/search'
r = requests.get(searchEngine, params = queryString)

print(r.url)
webbrowser.open(r.url)
