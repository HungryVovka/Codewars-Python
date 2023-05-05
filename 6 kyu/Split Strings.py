# -----------------------------------------------------------
# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should 
# replace the missing second character of the final pair with an underscore ('_').
# 
# Examples:
# 
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']
# -----------------------------------------------------------

def solution(s):
    arr = []
    if len(s) % 2 != 0:
        s += "_"
    letters = list(s)
    pair = ""
    for i in letters:
        pair += i
        if len(pair) == 2:
            arr.append(pair)
            pair = ""
    return arr

# or

def solution(s):
    arr = []
    if len(s) % 2 != 0:
        s += "_"
    for i in range(0, len(s), 2):
        arr.append(s[i:i + 2])
    return arr

# or

import re

def solution(s):
    arr = re.findall(".{2}", s + "_")
    return arr

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