# -----------------------------------------------------------
# Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.
# 
# Examples
# explode("312")
# 
# should return :
# 
# "333122"
# 
# explode("102269")
# 
# should return :
# 
# "12222666666999999999"
# -----------------------------------------------------------

def explode(s):
    arr = []
    s = list(s)
    for i in s:
        arr.append(i * int(i))
    return "".join(arr)

# or

def explode(s):
    return "".join(i * int(i) for i in s)

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