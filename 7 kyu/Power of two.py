# -----------------------------------------------------------
# Complete the function power_of_two/powerOfTwo (or equivalent, depending on your language) that determines if a given non-negative integer is a 
# power of two. From the corresponding Wikipedia entry:
# 
# a power of two is a number of the form 2n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the 
# exponent.
# 
# You may assume the input is always valid.
# 
# Examples
# power_of_two(1024) ==> True
# power_of_two(4096) ==> True
# power_of_two(333)  ==> False
# 
# Beware of certain edge cases - for example, 1 is a power of 2 since 2^0 = 1 and 0 is not a power of 2.
# -----------------------------------------------------------

def power_of_two(x):
    if x == 0:
        return False
    while x != 1:
        if x % 2 != 0:
            return False
        x = x // 2
    return True

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