# Given an array of numbers, sort the odd numbers in ascending order while leaving the even 
# numbers at their original positions.

# Examples: [7, 1]  =>  [1, 7]
#           [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
#           [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_odds(array):
  odds = sorted((element for element in array if element % 2 != 0), reverse=True)
  return [element if element % 2 == 0 else odds.pop() for element in array]

print(sort_odds([5, 8, 6, 3, 4]))
# Should print [3, 8, 6, 5, 4].

print(sort_odds([4, 6, 7, 3, 9, 2, 1, 0, 4, 3, 5]))

