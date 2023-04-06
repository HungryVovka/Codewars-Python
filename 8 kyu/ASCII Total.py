# -----------------------------------------------------------
# You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all ASCII characters.
# 
# examples:
# 
# uniTotal("a") == 97 uniTotal("aaa") == 291
# -----------------------------------------------------------

def uni_total(s):
    total = 0
    s = list(s)
    for i in s:
        total += ord(i)
    return total

# or

def uni_total(s):
    return sum(map(ord, s))

# or

def uni_total(s):
    return sum(ord(i) for i in s)

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