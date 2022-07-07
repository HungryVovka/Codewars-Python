# -----------------------------------------------------------
# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including 
# them.
# 
# For example:
# 
# a = 1
# b = 4
# --> [1, 2, 3, 4]
# -----------------------------------------------------------

def between(a,b):
    i = 1
    arr = []
    arr.append(a)
    while i <= (b - a):
        arr.append(a + i)
        i += 1
    return(arr)