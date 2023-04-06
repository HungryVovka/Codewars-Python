# -----------------------------------------------------------
# Write a method, that will get an integer array as parameter and will process every number from this array.
# 
# Return a new array with processing every number of the input-array like this:
# 
# If the number has an integer square root, take this, otherwise square the number.
# 
# Example
# [4,3,9,7,2,1] -> [2,9,3,49,4,1]
# 
# Notes
# The input array will always contain only positive numbers, and will never be empty or null.
# -----------------------------------------------------------

def square_or_square_root(arr):
    sqrt_it = 0.5
    new_arr = []
    for number in arr:
        if (number % pow(number, sqrt_it)) == 0:
            new_arr.append(int(pow(number, sqrt_it)))
        else:
            new_arr.append(int(number*number))
    return(new_arr)

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