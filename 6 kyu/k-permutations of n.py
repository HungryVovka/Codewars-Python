# -----------------------------------------------------------
# Implement a function k_permutations_of_n that accepts a list of elements lst and an integer k, and returns all permutations of elements from 
# the list lst. Permutations should be a list containing all unique lists of k elements from lst, in any order.
# 
# For example, if lst == [1,2,3] and k == 2 the result should be:
# 
# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
# 
# if k > len(lst) the function should return an empty list, i.e.[]
# if k == 0, the function should return [[]], because there is exactly 1 way to arrange 0 elements (remember that 0! == 1).
# 
# You can assume that the input list lst contains unique elements.
# -----------------------------------------------------------

from itertools import permutations

def k_permutations_of_n(lst, k):
    return [list(i) for i in permutations(lst, k)]

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