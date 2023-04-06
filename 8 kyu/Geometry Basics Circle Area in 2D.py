# -----------------------------------------------------------
# This series of katas will introduce you to basics of doing geometry with computers.
# 
# Write the function circleArea/CircleArea which takes in a Circle object and calculates the area of that circle.
# The Circle class can be seen below:
# 
# // Represents a Circle where center is a Point and radius is a Number
# class Circle {
#   constructor(center, radius) { 
#     this.center = center; 
#     this.radius = radius;
#   }
# }
# 
# And the Point class can be seen below:
# 
# // Represents a Point where x and y are Numbers
# class Point {
#   constructor (x,y) { 
#     this.x = x;
#     this.y = y; 
#   }
# }
# 
# Tests round answers to 6 decimal places.
# -----------------------------------------------------------

import math

def circle_area(circle):
    return math.pi * circle.radius**2

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