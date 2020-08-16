import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re
import csv
import getpass

# Ask user to type username and password

# Your login credentials
email = input("username[email id]: ") #your email id
password = getpass.getpass(prompt='Password: ', stream=None) # Your password

browser = webdriver.Chrome()
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
browser.maximize_window()

email_element = browser.find_element_by_id("username")
email_element.send_keys(email)

pass_element = browser.find_element_by_id("password")
pass_element.send_keys(password)
pass_element.submit()

print ("success! Logged in, Bot starting")
browser.implicitly_wait(3)

browser.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")

page = bs(browser.page_source, features="html.parser")
content = page.find_all('a', {'class':"mn-connection-card__link ember-view"})

mynetwork = []
for contact in content:
    mynetwork.append(contact.get('href'))
print(len(mynetwork), " connections")

my_network_emails = []
my_network_details = {}

# Connect to the profile of all contacts and save the email within a list
for contact in mynetwork:
    browser.get("https://www.linkedin.com" + contact + "detail/contact-info/")
    browser.implicitly_wait(2)
    contact_page = bs(browser.page_source, features="html.parser")

    # Get the name from <h1 id="pv-contact-info">
    contact_name = contact_page.find('h1', {'id': 'pv-contact-info'})
    contact_name = contact_name.text.strip()

    # for email id its a href: mailto
    content_contact_page = contact_page.find_all('a',href=re.compile("mailto"))

    for contact in content_contact_page:
        print("[+]", contact.get('href')[7:])
        my_network_details[contact_name] = {'email': contact.get('href')[7:]}

    # for mobile number : <li having this classpv-contact-info__ci-container>
    contact_phone = contact_page.find_all('li', {'class': 'pv-contact-info__ci-container'})
    # SAMPLE: <span class="t-14 t-black t-normal">xxxxxxxx</span>
    phone_number_regex = re.compile(r'\d{10}')
    phone_numbers = phone_number_regex.findall(str(contact_phone))

    for number in phone_numbers:
        print("[+]", number)
        my_network_details[contact_name].update({'phone_number': number})
    # wait few seconds before to connect to the next profile
    time.sleep(random.uniform(0.5, 1.1))

with open(f'new_contacts.csv', 'w') as f:
    writer = csv.writer(f)
    for name, contact_details_dict in my_network_details.items():
        if 'phone_number' in contact_details_dict:
            writer.writerow( [name, contact_details_dict['email'], contact_details_dict['phone_number'] ])
        else:
            writer.writerow( [name, contact_details_dict['email'] ])


browser.quit()
