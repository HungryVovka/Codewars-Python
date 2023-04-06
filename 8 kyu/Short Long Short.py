# -----------------------------------------------------------
# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. 
# The strings will not be the same length, but they may be empty ( zero length ).
# 
# Hint for R users:
# 
# The length of string is not always the same as the number of characters
# For example: (Input1, Input2) --> output
# 
# ("1", "22") --> "1221"
# ("22", "1") --> "1221"
# -----------------------------------------------------------

def solution(a, b):
    arr = []
    if len(a) > len(b):
        arr.insert(0, b)
        arr.append(a)
        arr.append(b)
    if len(a) < len(b):
        arr.insert(0, a)
        arr.append(b)
        arr.append(a)
    answer = "".join(arr)
    return (answer)

# or

def solution(a, b):
    return b + a + b if len(a) > len(b) else a + b + a

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