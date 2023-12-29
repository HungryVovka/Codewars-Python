# -----------------------------------------------------------
# Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?
# 
# Examples:
# 
# input:    output:
# 0    ->   0
# 2    ->   5
# 3    ->   5
# 12   ->   15
# 21   ->   25
# 30   ->   30
# -2   ->   0
# -5   ->   -5
# etc.
# 
# Input may be any positive or negative integer (including 0).
# 
# You can assume that all inputs are valid integers.
# -----------------------------------------------------------

def round_to_next5(n):
    remainder = n % 5
    return n if remainder == 0 else n - remainder + 5

# or

def round_to_next5(n):
    return (5 - n) % 5 + n

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