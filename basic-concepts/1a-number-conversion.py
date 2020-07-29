#!/usr/bin/python

# This tutorial will cover the concept of numeric type conversion in Python3.x

# Int
positive_int = 55

# Float
negative_float = -2.9987654

# Complex 
complex_num = 1j

# convert from int to float: 
positive_float = float(positive_int)  

# convert from float to int:
negative_int = int(negative_float)  

# convert from int to complex: 
complex_from_int = complex(positive_int)  

print(positive_float) 
print(negative_int) 
print(complex_from_int)  

print(type(positive_float)) 
print(type(negative_int)) 
print(type(complex_from_int))
