# -----------------------------------------------------------
# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# 
# What if the string is empty? Then the result should be empty object literal, {}.
# -----------------------------------------------------------

def count(s):
    answer = {}
    for i in s:
        if i not in answer:
            answer[i] = 1
        else:
            answer[i] += 1
    return answer

# or

def count(s):
    return {i : s.count(i) for i in s}

# or

import collections

def count(s):
    return collections.Counter(s)

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