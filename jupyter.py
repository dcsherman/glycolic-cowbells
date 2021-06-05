import requests
url = 'https://geo.craigslist.org/iso/us'
headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)'}
response = requests.get(url, headers=headers)
response.status_code
response.headers
response.content
print response

# https://charleston.craigslist.org