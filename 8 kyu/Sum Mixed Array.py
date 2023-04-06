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