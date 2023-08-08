# -----------------------------------------------------------
# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
# 
# Example 1:
# a1 = ["arp", "live", "strong"]
# 
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# 
# returns ["arp", "live", "strong"]
# 
# Example 2:
# a1 = ["tarp", "mice", "bull"]
# 
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# 
# returns []
# 
# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: In some languages r must be without duplicates.
# -----------------------------------------------------------

def in_array(a1, a2):
    answer = []
    for i in a1:
        for j in a2:
            if i in j and i not in answer:
                answer.append(i)
                continue
    return sorted(answer)

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