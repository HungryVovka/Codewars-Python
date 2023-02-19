# -----------------------------------------------------------
# Your task is to write function factorial.
# 
# https://en.wikipedia.org/wiki/Factorial
# -----------------------------------------------------------

def factorial(n):
    answer = 1
    while n > 0:
        answer *= n
        n -= 1
    return answer

# or

import math

def factorial(n):
    return math.factorial(n)