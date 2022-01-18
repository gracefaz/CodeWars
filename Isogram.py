# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.

# Example: If the word "Abba" in inputted, the function will output False. If the word "Bird" is
# inputted, then the function will output True.

def is_isogram(word):
    word = word.lower()
    for letter in word:
        if word.count(letter) > 1: return False
    return True

print(is_isogram("tree"))
# Prints False.

print(is_isogram("bird"))
# Prints True.