# Given a list of integers, determine whether the sum of its elements is odd or even.

# Example: [0, 1, 4] will print "odd" because 0 + 1 + 4 = 5 is odd.

# list = [0, 1, 4]
# print(sum(list))

def even_or_odd(list):
    if sum(list) % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd([0, 1, 4, 7, 8, 3, 1]))
# Prints "Even" as sum is 24.

print(even_or_odd([8, 7, 9, 4, 1]))
# Prints "Odd" as sum is 29.