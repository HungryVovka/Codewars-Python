# -----------------------------------------------------------
# Basic regex tasks. Write a function that takes in a numeric code of any length. The function should check if the code begins with 1, 2, or 3 and return 
# true if so. Return false otherwise.
# 
# You can assume the input will always be a number.
# -----------------------------------------------------------

def validate_code(code):
    return str(code).startswith("1") or \
        str(code).startswith("2") or \
        str(code).startswith("3")

# or

def validate_code(code):
    return str(code).startswith(("1", "2", "3"))

# or

import re

def validate_code(code):
    return bool(re.match("[123]", str(code)))

# or

def validate_code(code):
    return str(code)[0] in "123"

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