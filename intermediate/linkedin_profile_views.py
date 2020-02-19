import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import re # module for regular expression activities
import getpass # invisible password in terminal

# This script is to list the linkedin viewers for your profile
# Thanks to Prudhvi Pentakota for sharing this idea
# It's a web scraping, it might not work, if linkedin changes the code or
# Linkedin may block your IP too. So, don't run this script more often
# You can better use Linkedin developer API, if that allows you to view the list without being a paid member.
# AUTHOR: Sanjeev Jaiswal
# VERSION: 1.1

# Ask user to type username and password

# Your login credentials
email = input("username: ") #your email id
password = getpass.getpass(prompt='Password: ', stream=None) # Your password

# Leverage session of requests module
client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'
PROFILE_VIEWS_URL = 'https://www.linkedin.com/me/profile-views/urn:li:wvmp:summary/'

# It is to get loginCsrfParam value which is needed while logging in
html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html, "html.parser")
csrf = soup.find('input', {'name': 'loginCsrfParam'}).get('value')

# Building the payload to login
login_information = {
    'session_key': email,
    'session_password': password,
    'loginCsrfParam': csrf,
    'trk': 'guest_homepage-basic_sign-in-submit'
}

# Login with login_information data
client.post(LOGIN_URL, data=login_information)

# Get the content from profile views summary page
profile_views_raw = client.get(PROFILE_VIEWS_URL).content

# Give it an html view
profile_views_html = BeautifulSoup(profile_views_raw, "html.parser")

# look for <code id="bpr-guid-" and get the value
code = profile_views_html.findAll('code', {'id': re.compile('^bpr-guid-')})

final_viewer_list = []

for line in code:
    string_line = str(line)
    profile_search = re.findall('firstName":"(\w+)","lastName":"(\w+)"', string_line)
    if profile_search:
        final_viewer_list.extend(profile_search)

# using join() + map(), joining tuple elements
viewer_name_list = list(map(" ".join, final_viewer_list))

# unique values in list
viewer_name_list = list(set(viewer_name_list))

# sort the name list, case insensitive sorting
viewer_name_list.sort(key=lambda v: v.upper())

print("{} viewers have visited your LinkedIn profile today".format(len(viewer_name_list)))

count = 0

# printing nicely the viewer lists
for fullname in viewer_name_list:
    count+=1
    print(str(count) + ". " + fullname)

