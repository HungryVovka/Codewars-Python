# -----------------------------------------------------------
# Complete the function which converts a binary number (given as a string) to a decimal number.
# -----------------------------------------------------------

def bin_to_decimal(inp):
    num = 0
    for i in range(len(inp)):
        if inp[i] == "1":
            num += 2 ** (len(inp) - i - 1)
    return num

# or

def bin_to_decimal(inp):
    return int(inp, 2)

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