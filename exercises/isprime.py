#!/usr/bin/python3

# Exercise for if else and for loop
# Script to say if a number is prime or not
# If a number is divisible by only 1 and number itself, then it is a prime number

# Get input from user, as input is string, you would need to typecast it as an int
try:
    num = int(input('Enter a number: '))
except:
    exit("Only integer please!")


# Check if number is negative
if num < 0:
    exit('Number should be positive')
# If number is positive then write the logic of prime number
else:
    for prime in range(2, num):
        if (num % prime)== 0:
            print(num, 'is not a prime number')
            break
    else:
        print(num, 'is a prime number')

