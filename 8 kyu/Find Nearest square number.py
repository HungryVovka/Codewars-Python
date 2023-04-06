# -----------------------------------------------------------
# Your task is to find the nearest square number, nearest_sq(n), of a positive integer n.
# 
# Goodluck :)
# 
# Check my other katas:
# 
# Alphabetically ordered
# 
# Case-sensitive!
# 
# Not prime numbers
# -----------------------------------------------------------

import math

def nearest_sq(n):
    sq_before = int(math.sqrt(n))**2
    sq_after = (int(math.sqrt(n)) + 1)**2
    if abs(n - sq_before) < abs(n - sq_after):
        return sq_before
    else:
        return sq_after

# or

def nearest_sq(n):
    return round(n**0.5)**2

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