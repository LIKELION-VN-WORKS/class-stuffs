import requests, json

github_url = 'https://api.github.com/user/repos'
data = json.dumps({'name' : 'tests', 'descrpition':'desc'})
r = requests.post(github_url, data=data, auth=('dhy04057@likelion.org', 'adultlionmc18'))

print(r.json)
