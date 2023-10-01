# -----------------------------------------------------------
# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise 
# returns false.
# 
# Notes:
# 
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# 
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False
# -----------------------------------------------------------

def scramble(s1, s2):
    chars_count = [0] * 26
    for i in s1:
        chars_count[ord(i) - ord('a')] += 1
    for j in s2:
        chars_count[ord(j) - ord('a')] -= 1
        if chars_count[ord(j) - ord('a')] < 0:
            return False
    return True

# or

def scramble(s1, s2):
    return all(s1.count(i) >= s2.count(i) for i in set(s2))

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