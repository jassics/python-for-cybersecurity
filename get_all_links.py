import requests
import sys
import re
from bs4 import BeautifulSoup as bs

if len(sys.argv) != 2 :
    print("Please pass url")
    print("Ex: python {} <url>".format(sys.argv[0]))
    exit(0)

url = sys.argv[1]

getpage = requests.get(url)  
getpage_soup = bs(getpage.text, 'html.parser')
all_links= getpage_soup.findAll('a', attrs={'href' : re.compile("^https?://")})


for link in all_links:
    print(link.get('href'))

