# You are asked to square every digit of a number and concatenate them.

# Example: If we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.
# Note: The function accepts an integer and returns an integer

def square_every_digit(number):
    ret = ""
    for x in str(number):
        ret += str(int(x)**2)
    return int(ret)

print(square_every_digit(72))
# Prints 494.

print(square_every_digit(8746))
# Prints 64491636.