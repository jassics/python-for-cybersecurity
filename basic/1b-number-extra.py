#!/usr/bin/python
from decimal import Decimal as D

# In this example, we will cover
# 1. How float number works and why comparison on float suprise you
# 2. How to use Decimal format just like school days by using decimal module
# 3. Binary, octal and hex representation
# 4. Any mathematical operation of integer and float would result in float

# Integers can be of any length, a Floating point number is accurate only up to 15 decimal places
print((1.1 + 2.2) == 3.3)
print(1.1 + 2.2)

# Output: Decimal('3.3') 
print(D('1.1') + D('2.2'))  

# Output: Decimal('3.000') 
print(D('1.2') * D('2.50'))

#  ______________________________
# | Number System | Prefix       |
# | Binary        | '0b' or '0B' |
# | Octal         | '0o' or '0O' |
# | Hexadecimal   | '0x' or '0X' |
#  ------------------------------

# Output: 121
print(0b1111001)  
print(bin(121))

# Output: 257 (252 + 5) 
print(0xFC + 0b101)  
print(hex(252), bin(5))

# Output: 23 
print(0o27)
print(oct(23))

integer_num = 3
float_num = 1.7
sum_result = integer_num + float_num

# Output: sum_result = 4.7 and class float 
print(sum_result)
print(type(sum_result))
