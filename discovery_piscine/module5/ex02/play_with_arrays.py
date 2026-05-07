#!/usr/bin/env python3
array = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array: ", array)
for i in range(len(array)):
    array[i] = array[i] + 2
new_array = [x for x in array if x>5]
print("New array: ", new_array)
    
