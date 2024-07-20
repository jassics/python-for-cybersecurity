# Set is a collection of data which is unordered, unindexed and unique. It is one of the 4 native data types in Python
# This is based on a data structure concept hash table.
# We cannot access its elements by index like list
# Sets cannot have mutable items, otherwise it can contain mixed data

# Empty set initialization
# use set() method. Using {} will create empty dictionary
test = {}
# Output <class 'dict'>
print(type(test))
sets = set()
# Output <class 'set'>
print(type(sets))

# sets initialization
my_set = {1,2,3}
# Output {1, 2, 3}
print(my_set)

# or another way is using set() method
my_another_set = set([4,5,6])
# Output {4, 5, 6}
print(my_another_set)

# Add elements
# use set.add() method to add elements
for num in range(6):
    my_set.add(num)
# Output {0, 1, 2, 3, 4, 5}
print(my_set)

# Remove elements
# remove set items using remove() or discard() method
# if item doesn't exists remove() will raise an error, but discard() won't
my_set.remove(4)
# Output {0, 1, 2, 3, 5}
print(my_set)
my_set.discard(7)
# Output {0, 1, 2, 3, 5}
print(my_set)


# Union
# merging 2 sets using union() method or '|' operator
# it will return a new set
final_set = my_set.union(my_another_set)
# Output {0, 1, 2, 3, 4, 5, 6}
print(final_set)
same_set = my_set | my_another_set
# Output {0, 1, 2, 3, 4, 5, 6}
print(same_set)

# Update
# joining 2 sets using update() method
# it will update the set with another set data
my_set.update(my_another_set)
# Output {0, 1, 2, 3, 5, 4, 6}
print(my_set)


# Intersection
# Intersection of 2 sets using intersection() method or '&' operator
intersect = my_set.intersection(my_another_set)
# Output {4, 5, 6}
print(intersect)
intersect2 = my_set & my_another_set
# Output {4, 5, 6}
print(intersect2)

# Difference
# Difference of 2 sets using difference() method or '-' operator
diff = my_set.difference(my_another_set)
# output {0, 1, 2, 3}
print(diff)
diff2 = my_set - my_another_set
# Output {0, 1, 2, 3}
print(diff2)

# Symmetric Difference
# using symmetric_difference() method or '^' operator
# Output {0, 1, 2, 3}
print(my_set ^ my_another_set)
# Output {0, 1, 2, 3}
print(my_set.symmetric_difference(my_another_set))
# Output {0, 1, 2, 3}
print(my_another_set.symmetric_difference(my_set))

# Clear the set
intersect2.clear()
# Output set()
print(intersect2)

# Iterating through sets
for num in my_set:
    print(num)

# del keyword will delete the set completely
# del my_set

# ONE MORE THING
# Just like tuples is an immutable list, frozenset is an immutable sets
# imm_set = frozenset([1, 2, 3, 4])