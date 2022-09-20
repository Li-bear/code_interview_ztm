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


from operator import truediv


array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', '4']

def contains_common_item(arr1, arr2):
    arr_dict = convert_dict(arr1) # O(len(dict))
    print(is_there_repeated(arr_dict, arr2)) # O(n)


def convert_dict(arr):
    # Complexities for Creating a Dictionary:
    # Time complexity: O(len(dict))
    # Space complexity: O(n)
    arr_dict = {}
    for item in arr:
        if item in arr_dict.keys():
            arr_dict[item] += 1
        else:
            arr_dict[item] = 1
    return arr_dict


def is_there_repeated(arr_dict, arr_2compare):
    for item in arr_2compare:
        if (item in arr_dict.keys()):
            return True
    return False

# if we sort elements considering that characters are code in ASCII? 
# and later use binary search to fin the common item O(m*log(n))

contains_common_item(array1, array2)