# -----------------------------------------------------------
# The BOPE is the squad of special forces of police that usually handles the operations in the Favelas in Rio de Janeiro.
# 
# In this Kata you have to write a function that determine the number of magazines that every soldier has to have in his bag.
# 
# You will receive the weapon and the number of streets that they have to cross. Considering that every street the officer shoots 3 times. Bellow there 
# is the relation of weapons:
# 
# PT92 - 17 bullets
# M4A1 - 30 bullets
# M16A2 - 30 bullets
# PSG1 - 5 bullets
# 
# Example:
# 
# ["PT92", 6] => 2 (6 streets 3 bullets each)
# ["M4A1", 6] => 1
# 
# The return Will always be an integer so as the params.
# -----------------------------------------------------------

import math
from typing import Tuple

def mag_number(info: Tuple[str, int]) -> int:
    if "PT92" in info:
        return math.ceil((info[1] * 3) / 17)
    if "M4A1" in info:
        return math.ceil((info[1] * 3) / 30)
    if "M16A2" in info:
        return math.ceil((info[1] * 3) / 30)
    if "PSG1" in info:
        return math.ceil((info[1] * 3) / 5)

# or

import math

def mag_number(info):
    weapons = {
        "PT92": 17, 
        "M4A1": 30, 
        "M16A2": 30, 
        "PSG1": 5,
    }
    return math.ceil(info[1] * 3 / weapons[info[0]])

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