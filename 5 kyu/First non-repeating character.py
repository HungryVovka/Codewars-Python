# -----------------------------------------------------------
# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in 
# the string.
# 
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the 
# string.
# 
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the 
# initial letter. For example, the input 'sTreSS' should return 'T'.
# 
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
# -----------------------------------------------------------

def first_non_repeating_letter(s):
    s_upper = s.upper()
    for i in s_upper:
        if s_upper.count(i) == 1:
            return s[s_upper.index(i)]
    return ""

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