# -----------------------------------------------------------
# Task
# Given a string, return if a given letter always appears immediately before another given letter.
# 
# Worked Example
# ("he headed to the store", "h", "e") ➞ True
# 
# # All occurences of "h": ["he", "headed", "the"]
# # All occurences of "h" have an "e" after it.
# # Return True
# 
# ('abcdee', 'e', 'e') ➞ False
# 
# # For first "e" we can get "ee"
# # For second "e" we cannot have "ee"
# # Return False
# 
# Examples
# ("i found an ounce with my hound", "o", "u") ➞ True
# 
# ("we found your dynamite", "d", "y") ➞ False
# 
# Notes
# All sentences will be given in lowercase.
# -----------------------------------------------------------

def best_friend(txt, a, b):
    return txt.count(a) == txt.count(a + b)

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