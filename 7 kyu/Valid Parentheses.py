# -----------------------------------------------------------
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the 
# string is valid, and false if it's invalid.
# 
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# 
# Constraints
# 0 <= length of input <= 100
# 
# All inputs will be strings, consisting only of characters ( and ).
# Empty strings are considered balanced (and therefore valid), and will be tested.
# For languages with mutable strings, the inputs should not be mutated.
# 
# Protip: If you are trying to figure out why a string of parentheses is invalid, paste the parentheses into the code editor, and let the code highlighting 
# show you!
# -----------------------------------------------------------

def valid_parentheses(paren_str):
    while "()" in paren_str:
        paren_str = paren_str.replace("()", "")
    return paren_str == ""

# or

import re

def valid_parentheses(paren_str):
    try:
        re.compile(paren_str)
        return True
    except:
        return False

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