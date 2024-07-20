import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import re # module for regular expression activities
import getpass # invisible password in terminal
import sys

# This script is to list the linkedin viewers for your profile
# Thanks to Prudhvi Pentakota for sharing this idea
# Thanks to Sujay Gankidi for validating the script and output.
# It's a web scraping, it might not work, if linkedin changes the code or
# Linkedin may block your IP too. So, don't run this script more often
# You can better use Linkedin developer API, if that allows you to view the list without being a paid member.
# AUTHOR: Sanjeev Jaiswal
# VERSION: 1.2

# This script will ask creds if you pass online in argument,
# If you have opted for offline in argument then
# It will ask for file in txt format containing page-source of view-source:https://www.linkedin.com/me/profile-views/urn:li:wvmp:summary/
# (login first and open this url and save the contents in txt format)

def get_info_online():
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

    process_and_print(profile_views_raw)
    return None


def get_info_offline(filename):
    try:
        profile_views_raw = open(filename).read()
    except Exception as e:
        exit("Either file doesn't exit or you don't have permission. Please verify\n", e)

    process_and_print(profile_views_raw)
    return None


def process_and_print(raw_data):
    # Get raw content in html format
    profile_views_html = BeautifulSoup(raw_data, "html.parser")

    # look for <code id="bpr-guid-" and get the value
    code = profile_views_html.findAll('code', {'id': re.compile('^bpr-guid-')})

    if not code:
        exit("Possible wrong creds or data. Please check creds or contents and retry\n")

    final_viewer_list = []

    for line in code:
        string_line = str(line)
        # Below line was working earlier but now it's not working due to some changes at front-end
        # profile_search = re.findall('firstName":"(\w+\s?\w+?)","lastName":"([a-zA-z-,\.\s]+)"', string_line)

        # Below 3 lines are working code because you need to get firstname and lastname separately now and then zip it
        firstname = re.findall('firstName":"(\w+\s?\w+?)"', string_line)
        lastname = re.findall('lastName":"(\w+\s?\w+?)"', string_line)
        profile_search = zip(firstname,lastname)
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
        count += 1
        print(str(count) + ". " + fullname)

    return None


# We will use getopt or argparse or click to replace current sys.argv and if else block.
if len(sys.argv) >=2:
    if re.match(r'^online$', sys.argv[1], re.IGNORECASE):
        get_info_online()
    elif re.match(r'^offline$', sys.argv[1], re.IGNORECASE):
        if len(sys.argv) == 3:
            get_info_offline(sys.argv[2])
        else:
            exit("It requires filename when you choose offline option\npython script-name online or python script-name offline page-source.txt\n")
    else:
        exit("It should be either online or offline as an argument\npython script-name online or python script-name offline page-source.txt\n")
else:
    exit("It needs at least an argument\npython script-name online or python script-name offline page-source.txt\n")
