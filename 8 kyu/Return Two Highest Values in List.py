# -----------------------------------------------------------
# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.
# 
# The result should also be ordered from highest to lowest.
# 
# Examples:
# 
# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []
# -----------------------------------------------------------

def two_highest(arg1):
    arr = set(arg1)
    return sorted(arr, reverse = True)[:2]

# or

def two_highest(arg1):
    arr = list(set(arg1))
    arr.sort()
    return arr[-2:][::-1]