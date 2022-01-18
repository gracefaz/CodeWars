# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# Example: find_uniq([ 1, 1, 1, 2, 1, 1 ]) will output 2, find_uniq([ 0, 0, 0.55, 0, 0 ]) 
# # will output 0.55.

def find_uniq(arr):
    for n in arr:
        if arr.count(n) == 1:
            return n   

array = [4, 4, 4, 7, 4, 4]
print(find_uniq(array))
# Prints 7.

array2 = [2, 2, 2, 2, 2, 2, 2, 2, 9, 2]
print(find_uniq(array2))
# Prints 9.
