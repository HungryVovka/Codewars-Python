# -----------------------------------------------------------
# 1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246. Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681. The 
# sum of these squares is 84100 which is 290 * 290.
# 
# Task
# Find all integers between m and n (m and n integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.
# 
# We will return an array of subarrays or of tuples (in C an array of Pair) or a string. The subarrays (or tuples or Pairs) will have two elements: first the 
# number the squared divisors of which is a square and then the sum of the squared divisors.
# 
# Example:
# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]
# 
# The form of the examples may change according to the language, see "Sample Tests".
# 
# Note
# In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically 
# allocated character strings.
# -----------------------------------------------------------

import math

def square_division_check(n, sq_sum_div):
    arr = []
    if sq_sum_div != int(math.sqrt(sq_sum_div))**2:
        return None
    else:
        arr.append(n)
        arr.append(sq_sum_div)
        return arr

def sum_squared_divisors(n):
    i, sum_sq_divisor = 1, 0
    while i <= math.floor(math.sqrt(n)):
        if n % i == 0:
            sum_sq_divisor += i**2
            j = n // i
            if j != i:
                sum_sq_divisor += j**2
        i += 1
    return square_division_check(n, sum_sq_divisor)
    
def list_squared(m, n):
    answer = []
    i = m
    while i <= n:
        j = sum_squared_divisors(i)
        if j != None:
            answer.append(j)
        i += 1
    return answer

# -----------------------------------------------------------
# License
# Tasks are the property of Codewars (https://www.codewars.com/) 
# and users of this resource.
# 
# All solution code in this repository 
# is the personal property of Vladimir Rukavishnikov
# (vladimirrukavishnikovmail@gmail.com).
# 
# Copyright (C) 2022 Vladimir Rukavishnikov
# 
# This file is part of the HungryVovka/Codewars-Python
# (https://github.com/HungryVovka/Codewars-Python)
# 
# License is GNU General Public License v3.0
# (https://github.com/HungryVovka/Codewars-Python/blob/main/LICENSE.md)
# 
# You should have received a copy of the GNU General Public License v3.0
# along with this code. If not, see http://www.gnu.org/licenses/
# -----------------------------------------------------------