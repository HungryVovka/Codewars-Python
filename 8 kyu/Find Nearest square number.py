# -----------------------------------------------------------
# Your task is to find the nearest square number, nearest_sq(n), of a positive integer n.
# 
# Goodluck :)
# 
# Check my other katas:
# 
# Alphabetically ordered
# 
# Case-sensitive!
# 
# Not prime numbers
# -----------------------------------------------------------

import math

def nearest_sq(n):
    sq_before = int(math.sqrt(n))**2
    sq_after = (int(math.sqrt(n)) + 1)**2
    if abs(n - sq_before) < abs(n - sq_after):
        return sq_before
    else:
        return sq_after

# or

def nearest_sq(n):
    return round(n**0.5)**2