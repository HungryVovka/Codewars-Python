# -----------------------------------------------------------
# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).
# 
# If they are, change the array value to a string of that vowel.
# 
# Return the resulting array.
# -----------------------------------------------------------

def is_vow(inp):
    for i, j in enumerate(inp):
        if chr(j) in "aeiou":
            inp[i] = chr(j)
    return inp

# or

def is_vow(inp):
    return [chr(i) if chr(i) in "aeiou" else i for i in inp]

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