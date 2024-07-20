# Tuples is an immutable object in Python. It means once data is set, you cannot change those data.
# Can be used for constant data or dictionary without key (nested tuples)

# Empty Tuple initialization
tup = ()
print(tup)

# Tuple initialization with data
# I didn't like this way thought ;)
tup1 = 'python', 'aws', 'security'
print(tup1)

# Another for doing the same
tup2 = ('python', 'django', 'linux')
print(tup2)

# Concatenation
tup3 = tup1 + tup2
print(tup3)

# Nesting of tuples
tup4 = (tup1, tup2)
print(tup4)

# Length of a tuple
print(len(tup3))
print(len(tup4))

# Tuple Indexing and slicing
print(tup3[2])
print(tup2[1:])

# Deleting a tuple, removing individual element from the tuple is not possible. It deletes the whole tuple
del tup4

# Converts a list into tuple
tup5 = tuple(["Sanjeev", '2021', "Flexmind"])
print(tup5)

# try tuple() to a string
tup6 = tuple('Python')
print(tup6)

#Tuple iteration
for tup in tup5:
    print(tup)

# Max and min method
max_elem = max(tup1)
print("max element: ", max_elem)
print("min element: ", min(tup5))



