# -----------------------------------------------------------
# Jumps in a cycle [a1,...,an] can be written in a extended form with a jump rate equal to 1 as a1 -> a2 -> ... -> an -> a1 -> ... -> an...
# 
# Given a jump rate k and starting in the first element, you must find the number of jumps you have to take in order to reach the same element.
# 
# ASSUMPTION: The elements in the cycle are distinguishable.
# 
# Examples
# [1,5,7,8,9] and jump rate 1, then 1 -> 5 -> 7 -> 8 -> 9 -> 1. That is, 5 jumps.
# 
# [1,5,7,8,9] and jump rate 2, then 1 -> 7 -> 9 -> 5 -> 8 -> 1. That is, 5 jumps.
# 
# [1,5,1] and jump rate 2, then 1 -> 1 -> 5 -> 1. That is, 3 jumps.
# 
# Input
# cl: (list) the list with the cycle. 2 <= cl <= 2^30
# 
# k: (int) the jump rate. 1 <= k <= 2^40
# 
# Output
# (int) The number of jumps in order to reach the same first element in the cycle.
# -----------------------------------------------------------

import math

def get_jumps(cycle_list, k):
    return len(cycle_list) / math.gcd(len(cycle_list), k)

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