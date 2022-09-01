def print_hey(n):
    for i in range(0, len(n)): # O(n) bc it has one loop
        # are we adding any space inside this function? nope, so O(1)
        print("Hey!")

print_hey([1, 2, 3, 4, 5])

# Time complexity: O(n)
# Space complexity: an array is O(1)

def array_of_hi_n_times(n):
    # are we adding any space inside this function? yes
    # we are declaring a variable and a list
    hi_array = []
    for i in range(0, n): # O(n) bc it has one loop
        print(i)
        hi_array.append('hi') # each item is an additional memory space

    return hi_array

new_array = array_of_hi_n_times(6) # O(n) <- space complexity
print(new_array)