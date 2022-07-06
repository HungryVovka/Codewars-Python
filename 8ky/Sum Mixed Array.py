# -----------------------------------------------------------
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# 
# Return your answer as a number.
# -----------------------------------------------------------

def sum_mix(arr):
    summix = []
    for i in arr:
        summix.append(int(i))
    return sum(summix)

# or

def sum_mix(arr):
    summix = map(int, arr)
    return sum(summix)