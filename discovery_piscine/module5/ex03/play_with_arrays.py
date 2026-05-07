#!/usr/bin/env python3
array = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array:", array)

for i in range(len(array)):
    array[i] = array[i] + 2
new_array = [x for x in array if x>5]

print("New array:", new_array)

# This will print a set not in original order
# print("Set:", set(new_array))
#
# The fix is to use a dictionary
# ordered_set = list(dict.fromkeys(new_array))
# print("Set:", ordered_set)

# This fix uses a set() but with a list comprehension trick
seen = set()
ordered_set = [x for x in new_array if not (x in seen or seen.add(x))]
print("Set:", ordered_set)
