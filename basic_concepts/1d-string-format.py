#!/usr/bin/python
# Python has class str to represent and deal with string

first_name = "Sanjeev"
last_name  = 'Jaiswal'
nick_name  = '''Jassi'''
address    = """ Mailing Address right?
    if so, it's Hyderabad, Madhapur.
    Pin: 500081"""

mobile_num = 9618961800

text = ("Example of " + chr(37) + " operator:  %d is my number %s is my nick name. I have %.2f grands for %s" % (mobile_num, nick_name, 4.0, last_name))
print(text)

# Arguments by position
print("======== Arguments by position ========")
print("First Name: {}".format(first_name)) 
print("First Name: {0}".format(first_name))
print(f"First Name: {first_name}")
print("Full Name: {} {}".format(first_name, last_name))
print("Full Name: {0} {1}".format(first_name, last_name))
print("Full Name: {1} {0}".format(first_name, last_name))
print(f"Full Name: {first_name} {last_name}")

# Arguments by parameter
print("======= Arguments by parameter =======")
print("Nickname: {nick_name}".format(nick_name = "Jassi"))

# Output: 'Coordinates: 37.24N, -115.81W'
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))

full_name = {'first_name': 'Alicia', 'last_name': 'Gearcia'}
# Output 'Fullname: Gearcia Alicia'
print('Fullname: {last_name} {first_name}'.format(**full_name)) 
