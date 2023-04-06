# -----------------------------------------------------------
# In this kata, you need to write a function that takes a string and a letter as input and then returns the index of the second occurrence of that letter in 
# the string. If there is no such letter in the string, then the function should return -1. If the letter occurs only once in the string, then -1 should also be 
# returned.
# 
# Examples:
# 
# second_symbol('Hello world!!!','l') --> 3
# second_symbol('Hello world!!!', 'A') --> -1
# 
# Good luck ;) And don't forget to rate this Kata if you liked it.
# -----------------------------------------------------------

def second_symbol(s, symbol):
    i = 0
    for a, b in enumerate(s):
        if b == symbol:
            if i == 1:
                return a
            else:
                i += 1
    return -1

# or

def second_symbol(s, symbol):
    first = s.find(symbol)
    return s.find(symbol, first + 1)

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