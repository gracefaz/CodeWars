# Given n, take the sum of the digits of n. If that value has more than one digit, continue 
# reducing in this way until a single-digit number is produced. The input will be a non-negative 
# integer.

# Examples: 16  -->  1 + 6 = 7
#          942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
#       132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6

def digital_root(n):
    while n > 9:
        n = sum(int(i) for i in str(n))
    return n

print(digital_root(7364774874))
# Should print 3:
# 7 + 3 + 6 + 4 + 7 + 7 + 4 + 8 + 7 + 4 = 57
# 5 + 7 = 12
# 1 + 2 = 3
