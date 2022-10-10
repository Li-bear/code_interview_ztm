# Exercise
# Collection of numbers, take the maching par that is 
# equal to a sum that is given by the user.
# [1, 2, 3, 4] sum = 8 -> no
# [1, 2, 4, 4] sum = 8 -> yes

# Key points: one array not neccesarily sorted
# input: one array of any length and a integer
# output: boolean

# brute approach: nested loop
# complexity of O(n^2)

# smarter approach:
# Create a set with the complements
# check later if there is already the complemen in the set
# set.add worst case: O(n)
# search in a set worst case: O(n)

def find_pair_sum(arr, sum):
    complement = set()
    for number in arr:
        if number in complement:
            return True
        complement.add(sum - number)
    return False

def main():
    arr1 = [1, 3, 4, 5, 8, 12]
    # it works for no params and 0
    print(find_pair_sum(arr1, 8))


if __name__ == '__main__':
    main()