import requests

GOOGLE_MAP_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

params = {
    'address' : 'ho chi minh',
    'key': 'AIzaSyAGEzB0B9xZGCf9Qh8CXNhfRZKhXYfbiUI'
}

req = requests.get(GOOGLE_MAP_API_URL, params=params)
print(req.url)

res = req.json()['results']
location = res[0]['geometry']['location'] #안쪽으로 들어가는 부분 설명을 좀 더 자세히 해 드리기
location['lat']
location['lng']
print(location['lat'], location['lng'])
