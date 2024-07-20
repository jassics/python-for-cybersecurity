#!/usr/bin/python

# Python has class str to represent and deal with string

first_name = "Sanjeev"
last_name  = 'Jaiswal'
nick_name  = '''Jassi'''
address    = """ Mailing Address right?
    if so, it's Hyderabad, Madhapur.
    Pin: 500081"""

mobile_num = 9618961800

print("First Name:", first_name)
print("First Name: " + first_name) # String Concatenation
print("Multi line address string: " + address)

greetings = 'Howdy'   
print("Length of the string is " + str(len(greetings))) # len() for the length of the string

print(greetings + nick_name)  ## Howdy Jassi. String Concatenation  

pi = 3.14   # text = 'The value of pi is ' + pi      ## NO, does not work 
text = 'The value of pi is '  + str(pi)  ## need specifically to convert number to str type to print
