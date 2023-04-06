# -----------------------------------------------------------
# This series of katas will introduce you to basics of doing geometry with computers.
# 
# Point objects have x, y attributes. Circle objects have center which is a Point, and radius, which is a number.
# 
# Write a function calculating circumference of a Circle.
# 
# Tests round answers to 6 decimal places.
# -----------------------------------------------------------

import math

def circle_circumference(circle):
    answer = 2 * circle.radius * math.pi
    return round(answer, 6)

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