# -----------------------------------------------------------
# Task
# Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. Note: The result should be a boolean value, instead 
# of a string.
# 
# The opposite means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's 
# a empty string. Also take note of the edge case - if both strings are empty then you should return false/False.
# 
# Examples (input -> output)
# "ab","AB"     -> true
# "aB","Ab"     -> true
# "aBcd","AbCD" -> true
# "AB","Ab"     -> false
# "",""         -> false
# -----------------------------------------------------------

def is_opposite(s1,s2):
    return s1.swapcase() == s2 and s1 != ""

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