# -----------------------------------------------------------
# Given a string, write a function that returns the string with a question mark ("?") appends to the end, unless the original string ends with a question 
# mark, in which case, returns the original string.
# 
# For example (Input --> Output)
# 
# "Yes" --> "Yes?" 
# "No?" --> "No?"
# -----------------------------------------------------------

def ensure_question(s):
    return s if s.endswith("?") else s + "?"

# or

def ensure_question(s):
    return s if "?" in s else s + "?"

# or

def ensure_question(s):
    return s.rstrip("?") + "?"

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