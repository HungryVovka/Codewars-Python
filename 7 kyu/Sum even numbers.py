# -----------------------------------------------------------
# Complete the function that takes a sequence of numbers as single parameter. Your function must return the sum of the even values of this sequence.
# 
# Only numbers without decimals like 4 or 4.0 can be even.
# 
# The input is a sequence of numbers: integers and/or floats.
# 
# Examples
# [4, 3, 1, 2, 5, 10, 6, 7, 9, 8]  -->  30   # because 4 + 2 + 10 + 6 + 8 = 30
# []                               -->  0
# -----------------------------------------------------------

def sum_even_numbers(seq): 
    arr = []
    for s in seq:
        if s % 2 == 0:
            arr.append(s)
        else:
            continue
    return(sum(arr))

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