#!/usr/bin/python3
import requests
import sys
from bs4 import BeautifulSoup
import re
import validators

if len(sys.argv) !=2:
     print("Please pass the TLD (url without http(s))")
     print("python {0} TopLevelDomain\nEx: python {0} theayurveda.org".format(sys.argv[0]))
     exit(0)

alexa_base_url = 'https://alexa.com/siteinfo/'
site_name = sys.argv[1]

def is_valid_domain(site_name):
    if validators.domain(site_name):
        return True
    else:
        return False

if not is_valid_domain(site_name):
    print("Not a valid domain format {0} Exiting...".format(site_name))
    print("Valid Top Level Domain looks like 'theayurveda.org' or 'www.theayurveda.org' ")
    exit(0)

url_for_rank = alexa_base_url + site_name

page = requests.get(url_for_rank)
soup = BeautifulSoup(page.content, 'html.parser')
country_rank = soup.find_all('span', class_='pull-right')
global_rank = soup.find_all('div', class_='rankmini-global')

try:
    match = re.search(r'[\d,]+', global_rank[0].text.strip())
    print("Global Rank: ", match.group())
except:
    print("No global rank found for ", site_name)

try:
    ranks = soup.find_all('div', id='CountryRank')
    ranks_list = ranks[0].text.strip().split("\n")

    print("Country Rank: ")
    for rank in ranks_list:
        if re.search(r'#\d+', rank):
            print("\t",rank)
except:
    print("No country rank was found for ", site_name)
