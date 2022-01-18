# Create a function that takes a list of non-negative integers and strings and returns a new 
# list with the strings filtered out.

# Examples: filter_list([1,2,'a','b']) outputs [1,2].
# filter_list([1,'a','b',0,15]) outputs [1,0,15].
# filter_list([1,2,'aasf','1','123',123]) outputs [1,2,123].

def filter_list(list):
    new_list = []
    for element in list:
        if type(element) is int:
            new_list.append(element)
    return new_list

print(filter_list([4, 5, "a", "b"]))
# Prints [4, 5].

print(filter_list(["c", "d", 6, 7, "e", "f", 8, 9]))
# Prints [6, 7, 8, 9]

# Code accepted by Codewars and submitted!