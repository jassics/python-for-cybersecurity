#!/usr/bin/python3
import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re
import csv
import getpass


def login():
    # Ask user to type username and password

    # Your login credentials
    email = input("username[email id]: ")  # your email id
    password = getpass.getpass(prompt='Password: ', stream=None)  # Your password

    # initialize chrome drive, open url and login with credentials provided
    browser = webdriver.Chrome()
    browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    browser.maximize_window()

    email_element = browser.find_element_by_id("username")
    email_element.send_keys(email)

    pass_element = browser.find_element_by_id("password")
    pass_element.send_keys(password)
    pass_element.submit()

    print("success! Logged in, Bot starting")

    return(browser)


def get_title_location(contact):
    # Get title and location from parsed html content
    contact_details_list = []

    # Get title
    # Sample <h2 class="mt1 t-18 t-black t-normal break-words">
    try:
        contact_title = contact.find('h2', {'class': 'mt1 t-18 t-black t-normal break-words'})
        contact_title = contact_title.text.strip()
        print("[+]", contact_title)
        contact_details_list.append(contact_title)
    except:
        contact_details_list.append("NA")

    # Get location
    # Sample li with class t-16 t-black t-normal inline-block
    try:
        contact_location = contact.find('li', {'class': 't-16 t-black t-normal inline-block'})
        contact_location = contact_location.text.strip()
        print("[+]", contact_location)
        contact_details_list.append(contact_location)
    except:
        contact_details_list.append("NA")

    return contact_details_list


def get_name_email_phone(contact):
    # Get Name, email and phone number from parsed html content
    contact_details_list = []
    # Get the name from <h1 id="pv-contact-info">
    try:
        contact_name = contact.find('h1', {'id': 'pv-contact-info'})
        contact_name = contact_name.text.strip()
        print("[+]", contact_name)
        contact_details_list.append(contact_name)
    except:
        contact_details_list.append('NA')

    # for email id its a href: mailto
    content_contact_page = contact.find_all('a', href=re.compile("mailto"))

    # to extract mail id
    if content_contact_page:
        for contacts in content_contact_page:
            print("[+]", contacts.get('href')[7:])
            if contacts.get('href')[7:]:
                contact_details_list.append(contacts.get('href')[7:])
    else:
        contact_details_list.append('NA')

    # for mobile number : <li having this classpv-contact-info__ci-container> pv-contact-info__ci-container t-14
    contact_phone = contact.find_all('li', {'class': 'pv-contact-info__ci-container t-14'})

    # SAMPLE: <span class="t-14 t-black t-normal">xxxxxxxx</span>
    # Regex to match any of these:
    # 9618967875
    # 09618967875
    # +919618967875
    # +91-9618967875
    # +91 9618967875
    # +919618-967-785
    # +91-9618-967-785
    # +910 9618-967-785
    # (910) 987 7879

    # to extract phone number in possible manner with regex.
    if contact_phone:
        for phone in contact_phone:
            phone_number = phone.text.strip()
            phone_numbers = re.findall(r'^[(0+]?[\d\s]{1,3}?[-\s)]?[-\d\s]{8,12}$', phone_number, re.MULTILINE)

            if phone_numbers:
                for number in phone_numbers:
                    number.strip()
                    number.rstrip('\r\n')
                    if number:
                        print("[+]", number)
                        contact_details_list.append(number)
            else:
                contact_details_list.append('NA')
    else:
        contact_details_list.append('NA')

    # wait few seconds before to connect to the next profile
    time.sleep(random.uniform(0.8, 1.8))

    return contact_details_list


def get_contact_details(contact_url):
    # contact detail info popup url
    contact_detail_info = contact_url + "detail/contact-info"

    # get contact main page
    browser.get(contact_url)
    # get contact detail info popup page
    browser.get(contact_detail_info)
    # wait for 2 seconds for new contact
    browser.implicitly_wait(2)

    # for title and location
    contact_main_page = bs(browser.page_source, features="html.parser")
    title_location_list = get_title_location(contact_main_page)

    # for name, email and phone number
    contact_popup_page = bs(browser.page_source, features="html.parser")
    mail_phone_list = get_name_email_phone(contact_popup_page)

    return title_location_list + mail_phone_list


# MAIN SCRIPT START HERE
# Mode: Online or Offline
# Based on online or offline mode, you can run the script
# 1. Online: login and scroll the pages then save the connections url
# 2. Offline: pass connections url csv and then proceed with data extraction (Common for both mode)
mode = 'offline'  # mode can be 'online' or 'offline'
mynetwork = []  # mynetwork list contains contact urls


if mode == 'online':
    browser = login()
    browser.implicitly_wait(3)
    browser.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
    """
    SCROLL_PAUSE_TIME = 4.0
    try:
        for count in range(140):
            # Scroll down to bottom
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # in case loop terminates abruptly,
            page = bs(browser.page_source, features="html.parser")
            print(count)
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
    except:
        print("Exited for loop due to some fault.\n")
    """
    print("Processing connections page\n\n")
    page = bs(browser.page_source, features="html.parser")
    content = page.find_all('a', {'class': "mn-connection-card__link ember-view"})

    for contact in content:
        mynetwork.append(contact.get('href'))

    # Get all contact url in a text file for offline purpose to avoid scrolling long list of network main page
    f = open("fm-linkedin-contact-urls.txt", "a+")
    for contact_url in mynetwork:
        f.write(contact_url + "\n")
    f.close()

if mode == 'offline':
    f = open('fm-linkedin-contact-urls.txt')
    for url in f:
        url.strip()
        url.rstrip("\n")
        mynetwork.append(url)
    f.close()

print(len(mynetwork), " connections")

f = open('fm-linkedin-contacts.csv', 'a+')
writer = csv.writer(f)
writer.writerow(["Linkedin URL", "Name", "Title", "Location", "Email", "Phone"])

# Connect to the profile of all contacts and save the name, email, phone, title and location within a list
try:
    if mode == 'offline':
        browser = login()
    for contact in mynetwork:
        # Main url for contact
        contact_url = "https://www.linkedin.com" + contact
        contact_list = get_contact_details(contact_url)

        writer.writerow([contact_url, contact_list[2], contact_list[0], contact_list[1],
                      contact_list[3], contact_list[4]])
except:
    print("Processing Stopped\n")

f.close()
browser.quit()

