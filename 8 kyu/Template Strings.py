# -----------------------------------------------------------
# Template Strings
# Template Strings, this kata is mainly aimed at the new JS ES6 Update introducing Template Strings
# 
# Task
# Your task is to return the correct string using the Template String Feature.
# 
# Input
# Two Strings, no validation is needed.
# 
# Output
# You must output a string containing the two strings with the word ```' are '```
# Reference: https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/template_strings
# -----------------------------------------------------------

def temple_strings(obj, feature): 
    return f"{obj} are {feature}"

# or

temple_strings = "{} are {}".format

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