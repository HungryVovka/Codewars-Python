# -----------------------------------------------------------
# *** No Loops Allowed ***
# 
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value, without using a loop.
# 
# Array can contain numbers or strings. x can be either. Return true if the array contains the value, false if not. With strings you will need to 
# account for case.
# 
# Looking for more, loop-restrained fun? Check out the other kata in the series:
# 
# No Loops 1 - Small enough?
# -----------------------------------------------------------

def check(arr, item):
    return item in arr

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