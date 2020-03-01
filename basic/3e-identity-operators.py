#!/usr/bin/python

# Identity operators
# is and is not are the identity operators in Python.
# They are used to check if two values (or variables) are located on the same part of the memory.
# Two variables that are equal does not imply that they are identical.

# Example is taken from programiz.com
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

# Here, we see that x1 and y1 are integers of same values, so they are equal as well as identical.
# Same is the case with x2 and y2 (strings).
# But x3 and y3 are list. They are equal but not identical.
# It is because interpreter locates them separately in memory although they are equal.
