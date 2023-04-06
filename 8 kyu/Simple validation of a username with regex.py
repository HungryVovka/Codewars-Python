# -----------------------------------------------------------
# Write a simple regex to validate a username. Allowed characters are:
# 
# lowercase letters,
# numbers,
# underscore
# 
# Length should be between 4 and 16 characters (both included).
# -----------------------------------------------------------

def validate_usr(username):
    if 16 < len(username) or len(username) < 4:
        return False
    valid = "0123456789_abcdefghijklmnopqrstuvwxyz"
    for i in username:
        if i not in valid:
            return False
    return True

# or

def validate_usr(username):
    valid = "0123456789_abcdefghijklmnopqrstuvwxyz"
    if 16 >= len(username) >= 4 and all (i in valid for i in username):
        return True
    return False

# or

import re

def validate_usr(username):
    return re.match(r"^[0-9_a-z]{4,16}$", username) is not None

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