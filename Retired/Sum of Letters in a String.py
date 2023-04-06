# -----------------------------------------------------------
# In this kata, you are given a string.
# 
# The goal is to find the sum of all the letters in the string, where a = 1, b = 2...z = 26.
# 
# All other characters count for 0, and capitals are counted twice.
# 
# Example
# string_sum("abCd")
# 
# Should return 13, because a = 1, b = 2, c = 3 * 2, d = 4.
# 
# The sum is 1 + 2 + 6 + 4 = 13
# -----------------------------------------------------------

def string_sum(string):
    answer = 0
    for i in repr(string):
        if i.isalpha():
            letter = ord(i.lower()) - 96
            if i == i.lower():
                answer += letter
            else:
                answer += letter * 2
    return answer

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