# -----------------------------------------------------------
# This kata is from check py.checkio.org
# 
# You are given an array with positive numbers and a non-negative number N. You should find the N-th power of the element in the array with the 
# index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.
# 
# Let's look at a few examples:
# 
# array = [1, 2, 3, 4] and N = 2, then the result is 3^2 == 9;
# array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.
# -----------------------------------------------------------

def index(array, n):
    try:
        return array[n]**n
    except IndexError:
        return -1

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