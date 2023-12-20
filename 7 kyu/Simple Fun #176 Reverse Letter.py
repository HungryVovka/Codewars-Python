# -----------------------------------------------------------
# Task
# Given a string str, reverse it and omit all non-alphabetic characters.
# 
# Example
# For str = "krishan", the output should be "nahsirk".
# 
# For str = "ultr53o?n", the output should be "nortlu".
# 
# Input/Output
# [input] string str
# 
# A string consists of lowercase latin letters, digits and symbols.
# 
# [output] a string
# -----------------------------------------------------------

def reverse_letter(string):
    return "".join([i for i in string if i.isalpha()])[::-1]

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