# -----------------------------------------------------------
# vowelOne
# Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.
# 
# All non-vowels including non alpha characters (spaces,commas etc.) should be included.
# 
# Examples:
# 
# vowelOne "abceios" -- "1001110"
# 
# vowelOne "aeiou, abc" -- "1111100100"
# -----------------------------------------------------------

def vowel_one(s):
    s = s.lower()
    vowelOne = ""
    for i in s:
        if i in "aeiou":
            vowelOne += "1"
        else:
            vowelOne += "0"
    return vowelOne

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