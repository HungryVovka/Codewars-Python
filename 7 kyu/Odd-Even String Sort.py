# -----------------------------------------------------------
# Given a string s. You have to return another string such that even-indexed and odd-indexed characters of s are grouped and groups are space-
# separated (see sample below)
# 
# Note: 
# 0 is considered to be an even index. 
# All input strings are valid with no spaces
# 
# input: 'CodeWars'
# output 'CdWr oeas'
# 
# S[0] = 'C'
# S[1] = 'o'
# S[2] = 'd'
# S[3] = 'e'
# S[4] = 'W'
# S[5] = 'a'
# S[6] = 'r'
# S[7] = 's'
# 
# Even indices 0, 2, 4, 6, so we have 'CdWr' as the first group
# odd ones are 1, 3, 5, 7, so the second group is 'oeas'
# And the final string to return is 'Cdwr oeas'
# -----------------------------------------------------------

def sort_my_string(s):
    s = list(s)
    odd = list()
    even = list()
    for i in range(len(s)):
        if i == 0 or i % 2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    return "".join(even) + " " + "".join(odd)

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