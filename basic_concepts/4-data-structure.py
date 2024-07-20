# It's not new thing. In every programming language you would hear about its data structures.
# Data Structure is nothing but how you organize your data, how you display it, work on it and so on.
# Python has many inbuilt data structure which you have already faced like number, string
# We will discuss the most important Data Structure (DS) that you would be using more often in Python.
# They are:
# 1. List
# 2. Tuples
# 3. Dictionaries
# 4. Sets

# Please note there are many others with different python libraries like array.array but we won't discuss it as basics of Python

# List is a mutable DS and is implemented as dynamic array.
proto_list = ["http", "https", "ftp", "ssh"] # You can have list defined or create an empty list
print(proto_list)

# Tuples
# tuples are immutable object, otherwise it looks similar to list
# Immutable means elements can’t be added or removed dynamically and all the elements in a tuple must be defined at creation time.
proto_tuple = ("http", "https", "ftp", "ssh") # did you observe [] and (). [] means list and () means tuples here. Quite Interesting isn't it?
print(proto_tuple)

# Dictionaries
# Dictionaries in short we call Dict, stores an arbitrary number of objects, each identified by a unique key which will be always a string.
# Key will be string and value can be of any Python data type.
emp_id = {
    "sid": 657387,
    "daniel": 603719,
    "jassi": 770521,
}
print(emp_id)

# Sets
# A set is a collection of objects that don’t allow duplicate elements.
# Sets are unordered like dictionaries, so, you can't predict which would print first
# Sets are unchangeable, means once value is added, you can't edit it. However you can add new item
proto_set = {"tcp", "icmp", "ssh", "icmp", "ftp"} # Did you observe how its created? with {}. Now remember [], () and {} while creating these DS.
print(proto_set) # NO duplicate value ;)

# Also, {} means empty dictionary. Then what to use for empty set?