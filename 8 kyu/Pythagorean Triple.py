# -----------------------------------------------------------
# Given an array of 3 integers a, b and c, determine if they form a pythagorean triple.
# 
# A pythagorean triple is formed when:
# 
# c2 = a2 + b2
# where c is the largest value of a, b, c.
# 
# For example: a = 3, b = 4, c = 5 forms a pythagorean triple, because 52 = 32 + 42
# 
# Return Values
# 1 if a, b and c form a pythagorean triple
# 0 if a, b and c do not form a pythagorean triple
# For Python: return True or False
# -----------------------------------------------------------

def pythagorean_triple(integers):
    integers.sort()
    return integers[2]**2 - (integers[0]**2 + integers[1]**2) == 0

# or

def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return a * a + b * b == c * c

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