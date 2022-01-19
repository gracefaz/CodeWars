# Given an integral number, determine whether the number is a square number.

import math

def is_square(number):
    if number < 0:
        return False
    sqrt = math.sqrt(number)
    if sqrt.is_integer():
        return True
    else:
        return False

print(is_square(26))
# Returns "False"

print(is_square(49))
# Returns "True"

# Accepted by Codewars!