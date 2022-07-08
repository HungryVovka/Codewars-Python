# -----------------------------------------------------------
# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# 
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
# -----------------------------------------------------------

def grow(arr):
    answer = 1
    for i in arr:
        answer *= i
    return answer