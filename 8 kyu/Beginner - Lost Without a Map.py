# -----------------------------------------------------------
# Given an array of integers, return a new array with each value doubled.
# 
# For example:
# 
# [1, 2, 3] --> [2, 4, 6]
# -----------------------------------------------------------

def maps(a):
    arr = []
    for i in a:
        arr.append(i * 2)
    return arr