#!/usr/bin/python

# There is an array full of integers and there is a target value t, again an integer
# You need to find which of the 2 integers sums equal to target and print those 2 integers index number
# You can safely assume that there is only such pair which would result in sum as target

num_list = [2, 1, 3, 5, 6, 11, 2, 13, 4, 15]
target = 12

def twoSum(arr, t):
    index_dict = {}
    length = len(arr)
    index = 0

    while index < length:
        if (t - arr[index]) in index_dict:
            return index_dict[t - arr[index]], index
        index_dict[arr[index]] = index
        index += 1

print(twoSum(num_list, target))

