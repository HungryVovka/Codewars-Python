# -----------------------------------------------------------
# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered 
# even.
# 
# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
# 
# The input will be a lowercase string with no spaces.
# 
# Good luck!
# -----------------------------------------------------------

def capitalize(s):
    cap1, cap2 = [], []
    i = 0
    while i < len(s):
        if i % 2 == 0:
            cap1.append(s[i].upper())
            cap2.append(s[i].lower())
        else:
            cap1.append(s[i].lower())
            cap2.append(s[i].upper())
        i += 1
    return ["".join(cap1), "".join(cap2)]

# or

def capitalize(s):
    cap1, cap2 = [], []
    for i in range(len(s)):
        if i % 2 == 0:
            cap1.append(s[i].upper())
            cap2.append(s[i].lower())
        else:
            cap1.append(s[i].lower())
            cap2.append(s[i].upper())
        i += 1
    return ["".join(cap1), "".join(cap2)]

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