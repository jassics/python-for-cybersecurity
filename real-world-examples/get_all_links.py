import requests
import sys
import re
from bs4 import BeautifulSoup as bs
import validators

# Make sure url is passed as an argument
if len(sys.argv) != 2 :
    print("Please pass url")
    print("Ex: python {} <url>".format(sys.argv[0]))
    exit(0)

# save the command line argument for url in a variable
url = sys.argv[1]

# Exit if url is not valid
if not validators.url(url):
    exit("Not a valid url")

# get response of the url
get_content = requests.get(url)

# get html formatted content using bs module
getpage_soup = bs(get_content.text, 'html.parser')

# find all the links using a tag and with regex to look for href value as starting with http or https
all_links= getpage_soup.findAll('a', attrs={'href' : re.compile("^https?://")})

# Save the links in a file
# just get the domain name and create a file by domain name with -links.txt
domain_name = url.split('//')[1]
file_name = domain_name + '-links.txt'

with open(file_name, 'w+') as file_to_write:
    for link in all_links:
        href_link = link.get('href')
        if re.search("facebook|fb|instagram|linkedin|twitter|google|telegram|whatsapp|pinterest|goo\.gl|baidu", href_link) is None:
            file_to_write.write(href_link + "\n")
