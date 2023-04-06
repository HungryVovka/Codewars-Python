# -----------------------------------------------------------
# Complete the function circleArea so that it will return the area of a circle with the given radius. Round the returned number to two decimal 
# places (except for Haskell). If the radius is not positive or not a number, return false.
# 
# Example:
# 
# circleArea(-1485.86)     #returns False
# circleArea(0)            #returns False
# circleArea(43.2673)      #returns 5881.25
# circleArea(68)           #returns 14526.72
# circleArea("number")     #returns False
# -----------------------------------------------------------

import math

def circle_area(r):
    if not isinstance(r, int) or r <= 0:
        return False;
    return round(math.pi * r * r, 2)

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