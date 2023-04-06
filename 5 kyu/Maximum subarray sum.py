# -----------------------------------------------------------
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
# 
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# 
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only 
# negative numbers, return 0 instead.
# 
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
# -----------------------------------------------------------

def max_sequence(arr):
    maxsum = 0
    count = 0
    for i in arr:
        count = max(0, count + i)
        if count > maxsum:
            maxsum = count
    return maxsum

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