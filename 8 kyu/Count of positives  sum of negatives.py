# -----------------------------------------------------------
# Given an array of integers.
# 
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive 
# nor negative.
# 
# If the input is an empty array or is null, return an empty array.
# 
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
# -----------------------------------------------------------

def count_positives_sum_negatives(arr):
    pos_arr = []
    neg_arr = []
    if arr != []:
        for number in arr:
            if number > 0:
                pos_arr.append(number)
            if number < 0:
                neg_arr.append(number)
        new_arr = []
        new_arr.append(len(pos_arr))
        new_arr.append(sum(neg_arr))
        return(new_arr)
    else:
        return([])

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