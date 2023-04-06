# -----------------------------------------------------------
# Given a string s, write a method (function) that will return true if its a valid single integer or floating number or false if its not.
# 
# Valid examples, should return true:
# 
# isDigit("3")
# isDigit("  3  ")
# isDigit("-3.23")
# 
# should return false:
# 
# isDigit("3-4")
# isDigit("  3   5")
# isDigit("3 5")
# isDigit("zero")
# -----------------------------------------------------------

import re

def isDigit(string):
    return bool(re.match(r"^-?\d*\.?\d+$", string))

# or

def isDigit(string):
    try:
        float(string)
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