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

# List manipulation
# len() function
print("No of allowed ports in the list are: ", len(allowed_ports))
print("Allowed ports are: ", allowed_ports)

# count() function to count how many such entries are there
print("No. of port 80 in the list: ", allowed_ports.count(80))
print("No. of port 8001 in the list: ", allowed_ports.count(8001))

# index() function to find the index number of matched content in the list
print("Index of port 3306 in the list: ", allowed_ports.index(3306))

# See the difference between reversed() and reverse() function
print("\nWays to reverse the list")
reverse_port_list = list(reversed(allowed_ports))
print("Reverse of port list using reversed() method: ", reverse_port_list)

allowed_ports.reverse()
print("Reverse of port list using reverse() method:", allowed_ports)

# reversing it again to make it in ascending order :D
allowed_ports.reverse()

# sorted() function to sort a list quickly
print("\nWays to sort the list")
sorted_port_list = sorted(allowed_ports)
print("Sorted port list using sorted() method", sorted_port_list)

# Adding/Removing elements
print("\nWays to add elements")
# adds the items at the end of the list
allowed_ports.append(27018)
print(allowed_ports)

# Adding elements at 7th position, so index is 6
allowed_ports.insert(6,110)
print(allowed_ports)

print("\nWays to delete elements")
# remove() method removes the specified item
allowed_ports.remove(27018) # delete port 27018
print(allowed_ports)

# pop() method removes the specified index, (or the last item if index is not specified)
allowed_ports.pop(6) # delete 7th index
print(allowed_ports)

# del keywords removes at the specified index or even the whole list
del allowed_ports[0]
print(allowed_ports)
# Commented purposefully `del allowed_ports`

# clear method empties the list
allowed_ports.clear()
print(allowed_ports)

# lets delete the whole list now.
del allowed_ports
try:
    print(allowed_ports)
except Exception as e:
    print("Seems allowed_ports doesn't exist now? Error:", e)

# You can try below 2 tasks
# 1. Join the lists
# 2. Copy the lists
# Also, try to understand Shallow copy vs Deep copy


