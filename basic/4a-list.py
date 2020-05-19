#!/usr/bin/python

# Empty List
allowed_ports = []

# pre-defined list
allowed_ports = [22, 23, 25, 53, 80, 69, 443, 3306, 8000, 8080, 5439, 8081, 9001,27017]

# Iterate through the list
print("Iterate through the list")
for port in allowed_ports:
    print(port)

# Check if an element exists in the list
print("\nChecking if port 5432 is present in the approved list or not")
if 5432 in allowed_ports:
    print("Port Postgres default port 5432 is allowed")
else:
    print("Not Approved!\n\tYou need to take admin approval to enable port 5432 for postgres")

# Access the list
print("\nShowing some ways to access the contents of list items")
print("First element of the list {}".format(allowed_ports[0])) # First index of the list is 0
print("Last element of the list {}".format(allowed_ports[-1])) # -1 in list shows the last element
print("Range of 3rd to 6th elements of the list {}".format(allowed_ports[2:6])) # The search will start at index 2 (included) as it contains 3rd element and end at index 6 (not included) which means 7th element.
print("Items form the beginning till 8th element i.e port 3306 in our case {}".format(allowed_ports[:8]))
print("Items from 5th elemets to the end {}".format(allowed_ports[4:]))
print("Let's see if you understand slicing here {}".format(allowed_ports[-7:-2]))

# Change the vakue of exsiting element
print("\nChange the value of port 69 to 690, check 6th element")
print(allowed_ports)
allowed_ports[5] = 690
print(allowed_ports)


