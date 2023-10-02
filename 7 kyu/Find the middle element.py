# -----------------------------------------------------------
# As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between 
# the other two elements.
# 
# The input to the function will be an array of three distinct numbers (Haskell: a tuple).
# 
# For example:
# 
# gimme([2, 3, 1]) => 0
# 
# 2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.
# 
# Another example (just to make sure it is clear):
# 
# gimme([5, 10, 14]) => 1
# 
# 10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.
# -----------------------------------------------------------

def gimme(input_array):
    a, b, c = input_array
    if a < b < c or c < b < a:
        return 1
    elif b < a < c or c < a < b:
        return 0
    elif a:
        return 2

# or

def gimme(input_array):
    return input_array.index(sorted(input_array)[1])

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