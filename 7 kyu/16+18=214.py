# -----------------------------------------------------------
# For this kata you will have to forget how to add two numbers.
# 
# It can be best explained using the following meme:
# 248 + 208 = 4416
# 
# In simple terms, our method does not like the principle of carrying over numbers and just writes down every number it calculates :-)
# 
# You may assume both integers are positive integers.
# -----------------------------------------------------------

import math

def add(num1, num2):
    if num1 == 0 and num2 == 0:
        return 0
    else:
        sum214 = ""
        while num1 or num2:
            sum214 = str(num1 % 10 + num2 % 10) + sum214
            num1 = math.floor(num1 / 10)
            num2 = math.floor(num2 / 10)
        return int(sum214)