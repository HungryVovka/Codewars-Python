# -----------------------------------------------------------
# Complete the function that accepts a valid string and returns an integer.
# 
# Wait, that would be too easy! Every character of the string should be converted to the hex value of its ascii code, then the result should be the sum of 
# the numbers in the hex strings (ignore letters).
# 
# Examples
# "Yo" ==> "59 6f" ==> 5 + 9 + 6 = 20
# "Hello, World!"  ==> 91
# "Forty4Three"    ==> 113
# -----------------------------------------------------------

def hex_hash(code):
    return sum(map(int, filter(str.isdigit, code.encode().hex())))

# or

def hex_hash(code):
    return sum(int(y) for x in code for y in hex(ord(x)) if y.isnumeric())

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