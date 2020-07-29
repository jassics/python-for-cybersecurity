#!/usr/bin/python

# Control statement is one the important building block of Python
# We will cover
# 1. if elif else
# 2. while, for, range
# 3. break, continue, pass

# 1. Example of if, elif, else
# There can be zero or more elif statement
# else is optional

url = input("Enter your website: ")

if 'http' in url:
    print('not safe url')
elif 'https' in url:
    print('somehow safer')
elif url == 'cybercloud.guru':
    print('aha cybercloud guru found')
elif url == '':
    print('How a url can be blank? forgot to type?')
else:
    print('here is your url: ' + url)


