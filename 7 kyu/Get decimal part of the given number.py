# -----------------------------------------------------------
# Write a function that returns only the decimal part of the given number.
# 
# You only have to handle valid numbers, not Infinity, NaN, or similar. Always return a positive decimal part.
# 
# Examples
# get_decimal(2.4)  # 0.4
# get_decimal(-0.2) # 0.2
# -----------------------------------------------------------

def get_decimal(n): 
    return abs(n) % 1

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