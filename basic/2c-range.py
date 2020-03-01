#!/usr/bin/python

# Python built-in function range() generates the integer numbers between the given start integer to the stop integer, i.e., range() returns a range object.
# Using for loop, we can iterate over a sequence of numbers produced by the range() function.
# It only allows integer type numbers as arguments.
# We can’t provide a string or float type parameter inside the range() function.
# The arguments can either be +ve or -ve.
# It doesn’t accept ‘0’ as a step value. If the step is ‘0’, the function throws a ValueError.

for step in range(10, 100, 10):
    print(step)


print("\nAnother Example to loop over a list using range")
port_lists = [21, 22, 23, 25, 53, 80, 443, 3306, 8080, 9002, 27017]

for port in range(len(port_lists)):
    print(port_lists[port])
