# -----------------------------------------------------------
# You should write a simple function that takes string as input and checks if it is a 
# valid Russian postal code, returning true or false.
# 
# A valid postcode should be 6 digits with no white spaces, letters or other symbols. 
# Empty string should also return false.
# 
# Please also keep in mind that a valid post code cannot start with 0, 5, 7, 8 or 9
# 
# Examples
# Valid postcodes:
# 
# 198328
# 310003
# 424000
# 
# Invalid postcodes:
# 
# 056879
# 12A483
# 1@63
# 111
# -----------------------------------------------------------

import re   # fullmatch

def zipvalidate(postcode):
    return bool(re.fullmatch(r"[12346]\d{5}", postcode))

# -----------------------------------------------------------
# License
# Tasks are the property of Codewars (https://www.codewars.com/) 
# and users of this resource.
# 
# All solution code in this repository 
# is the personal property of Vladimir Rukavishnikov
# (vladimirrukavishnikovmail@gmail.com).
# 
# Copyright (C) 2025 Vladimir Rukavishnikov
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