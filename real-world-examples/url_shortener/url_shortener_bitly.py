# pip3 install pyshorteners
import pyshorteners
import requests

url = input("Long url: ")

# Shorteners with API key
# Bit.ly implementation through pyshorteners module
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
shortener = pyshorteners.Shortener(api_key=ACCESS_TOKEN)
print(shortener.bitly.short(url))

# Bit.ly implementation through API call
# https://dev.bitly.com/api-reference#createBitlink
headers = {
    'Authorization': 'Bearer {}'.format(ACCESS_TOKEN),
    'Content-Type': 'application/json',
}

data = { "long_url": url}
response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, json=data)
# SAMPLE OUTPUT
# {'created_at': '2021-07-17T11:15:50+0000', 'id': 'bit.ly/bit.ly/3imNqJf', 'link': 'https://bit.ly/3imNqJf', 'custom_bitlinks': [], 'long_url': 'https://www.flexmind.co/tutorials/javascript-essentials-course/', 'archived': False, 'tags': [], 'deeplinks': [], 'references': {'group': 'https://api-ssl.bitly.com/v4/groups/Bl79bPA90Jk'}}

print(response.json()['link'])
