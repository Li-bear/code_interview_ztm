# Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# For Example:
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# should return false.
# -----------
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
# should return true.

# 2 parameters - arrays - no size limit
# return true or false

# brute approach: nested loop, two for loops Big O(n^2) if the two arrays have the same size
# O(m * n) where m is size of array1 and n is size of array2


array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']

def contains_common_item(arr1, arr2):
    pass

# if we sort elements considering that characters are code in ASCII? 
# and later use binary search to fin the common item O(m*log(n))
