# -----------------------------------------------------------
# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
# 
# Note: anagrams are case insensitive
# 
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
# 
# Examples
# "foefet" is an anagram of "toffee"
# 
# "Buckethead" is an anagram of "DeathCubeK"
# -----------------------------------------------------------

def is_anagram(test, original):
    return sorted(list(test.lower())) == sorted(list(original.lower()))

# or

def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

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