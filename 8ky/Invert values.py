# -----------------------------------------------------------
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
# 
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# 
# You can assume that all values are integers. Do not mutate the input array/list.
# -----------------------------------------------------------

def invert(lst):
    arr = []
    if lst == arr:
        return arr
    else:
        for l in lst:
            arr.append(-l)
        return arr