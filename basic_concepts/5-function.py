#!/usr/bin/python

# Examples of function in Python 3.x

# When you need a function?
#   When you want to perform a set of specific tasks and want to reuse that code whenever required
#   Also, for better modularity, readability and troubleshooting

# How to write a function (Syntax)?
'''def function_name():
    {
        # some code here
    }
'''

# Different ways to pass parameters
# What to return through function

# A basic function of adding two numbers
def add_numbers(num1, num2):
    return num1+num2

# How to call a function?
# most basic way to call a function is `function_name()`
# Calling above function
print(add_numbers(5,4))

# Function to find if a number is even
def  is_even(num):
    if num%2 == 0:
        return True
    return False

num = 12
result = is_even(num)
if result:
    print(f'{num} is even')
else:
    print(f'{num} is not even')

