# Return the number (count) of vowels in the given string. We will consider a, e, i, o, u as 
# vowels for this Kata (but not y).The input string will only consist of lower case letters 
# and/or spaces.

# Example: "hi codecademy" will print 5.

def vowel_count(string):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for letter in list(string):
        if letter in vowels:
            count += 1
    return count

print(vowel_count("hi codecademy"))
# Prints 5.

print(vowel_count("codewars is really fun"))
# Prints 7.