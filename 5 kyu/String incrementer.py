# -----------------------------------------------------------
# Your job is to write a function which increments a string, to create a new string.
# 
# If the string already ends with a number, the number should be incremented 
# by 1.
# If the string does not end with a number. the number 1 should be appended 
# to the new string.
# Examples:
# 
# foo -> foo1
# 
# foobar23 -> foobar24
# 
# foo0042 -> foo0043
# 
# foo9 -> foo10
# 
# foo099 -> foo100
# 
# Attention: If the number has leading zeros the amount of digits should be 
# considered.
# -----------------------------------------------------------

import re   # search

def increment_string(strng: str) -> str:
    match_result = re.search(r"(\d+)$", strng)
    if not match_result:
        return strng + "1"
    number_str = match_result.group(1)
    prefix = strng[:match_result.start()]
    number_length = len(number_str)
    incremented_value = int(number_str) + 1
    incremented_str = str(incremented_value).zfill(number_length)
    return prefix + incremented_str

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