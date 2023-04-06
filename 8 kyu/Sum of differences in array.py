# -----------------------------------------------------------
# Your task is to sum the differences between consecutive pairs in the array in descending order.
# 
# Example
# [2, 1, 10]  -->  9
# In descending order: [10, 2, 1]
# 
# Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9
# 
# If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell, None in Rust).
# -----------------------------------------------------------

def sum_of_differences(arr):
    arr.sort()
    if len(arr) > 0:
        return(abs(arr[-1] - arr[0]))
    else:
        return(0)

# or

def sum_of_differences(arr):
    return max(arr) - min(arr) if len(arr) > 1 else 0

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