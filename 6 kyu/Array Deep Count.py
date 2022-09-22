# -----------------------------------------------------------
# len(a) will give you the number of top-level elements in the list/array named a.
# 
# Your task is to create a function deepCount that returns the number of ALL elements within an array, including any within inner-level arrays.
# 
# For example:
# 
# deepCount([1, 2, 3]);  
# //>>>>> 3
# deepCount(["x", "y", ["z"]]);  
# //>>>>> 4
# deepCount([1, 2, [3, 4, [5]]]);  
# //>>>>> 7
# 
# The input will always be an array.
# -----------------------------------------------------------

import functools

def deep_count(a):
    if not isinstance(a, list):
        return 0
    if len(a) == 0:
        return 0
    return len(a) + functools.reduce(lambda x, y : x + deep_count(y), a, 0)

# or

def deep_count(a):
    return sum(1 + (deep_count(i) if isinstance(i, list) else 0) for i in a)

# or

def deep_count(a):
    answer = 0
    for i in range(len(a)):
        if type(a[i]) is list:
            answer += deep_count(a[i])
        answer += 1
    return answer

# or

def deep_count(a):
    answer = 0
    for i in a:
        answer += 1
        if isinstance(i, list):
            answer += deep_count(i)
    return answer