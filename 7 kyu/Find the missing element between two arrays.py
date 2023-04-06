# -----------------------------------------------------------
# Given two integer arrays where the second array is a shuffled duplicate of the first array with one element missing, find the missing element.
# 
# Please note, there may be duplicates in the arrays, so checking if a numerical value exists in one and not the other is not a valid solution.
# 
# find_missing([1, 2, 2, 3], [1, 2, 3]) => 2
# find_missing([6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2]) => 8
# 
# The first array will always have at least one element.
# -----------------------------------------------------------

def find_missing(arr1, arr2):
    for i in arr2:
        arr1.remove(i)
    return arr1[0]

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