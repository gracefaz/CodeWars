# Your task is to make a function that can take any non-negative integer as an argument and 
# return it with its digits in descending order. Essentially, rearrange the digits to create 
# the highest possible number.

# Example: If the number 42145 was inputted, the output would be 54421.

def descending_order(number):
    if number <= 0:
        return "Input must be a non-negative integer."
    else:
        return int("".join(sorted(str(number), reverse=True)))

print(descending_order(74920))
# Prints 97420

print(descending_order(-27))
# Prints "Input must be a non-negative integer."