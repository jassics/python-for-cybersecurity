#!/usr/bin/python
# Python has class str to represent and deal with string

first_name = "Sanjeev"
last_name  = 'jaiswal'
nick_name  = '''Jassi'''
address    = """ Mailing Address right?
    if so, it's Hyderabad, Madhapur.
    Pin: 500081"""

mobile_num = 9618961800

greetings = 'Howdy'   
print("Length of the string is 'Howdy' is: " + str(len(greetings))) # len() for the length of the string

# lower(), upper() and capitalize() function examples
## howdy Jassi. String Concatenation  
print(greetings.lower(), nick_name)  

# Let's make names all CAPS
print(first_name.upper(), last_name.upper())

# Capitalize last_name
print(last_name.capitalize())

#------------------------------------------------------------------------------------------------------#
# Method                                | True (if)                                                      #
# str.isalnum()                         | String consists of only alphanumeric characters (no symbols) #
# str.isalpha()                         | String consists of only alphabetic characters (no symbols)   #
# str.islower()                         | String’s alphabetic characters are all lower case            #
# str.isupper()                         | String’s alphabetic characters are all upper case            #
# str.isnumeric()                       | String consists of only numeric characters                   #
#------------------------------------------------------------------------------------------------------#

print(str(mobile_num).isnumeric())
print(first_name.isalpha())
print(last_name.isalnum())
print(nick_name.isupper())

# join() and split() functions
reversed_first_name =''.join(reversed(first_name))
print("Reverse of {} is {}". format(first_name, reversed_first_name))

# Practice for split(), replace(), strip(), find()
# Check our Lab Practice Questions
