#!/usr/bin/python3

def fahr_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

try:
    fahr = int(input('Enter temperature in Fahrenheit please: '))
except:
    exit("I am sorry. Only real numbers are allowed")

print(fahr_to_cel(fahr))

