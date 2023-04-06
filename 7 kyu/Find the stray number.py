# -----------------------------------------------------------
# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# 
# Complete the method which accepts such an array, and returns that single different number.
# 
# The input array will always be valid! (odd-length >= 3)
# 
# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3
# -----------------------------------------------------------

def stray(arr):
    arr = sorted(arr)
    if arr[0] != arr[1]:
        return arr[0]
    return arr[len(arr) - 1]

# or

def stray(arr):
    return [i for i in arr if arr.count(i) == 1][0]

# or

def stray(arr):
    return min(arr, key = arr.count)

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