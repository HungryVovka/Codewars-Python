# -----------------------------------------------------------
# This series of katas will introduce you to basics of doing geometry with computers.
# 
# Point objects have x and y attributes (X and Y in C#) attributes.
# 
# Write a function calculating distance between Point a and Point b.
# 
# Tests round answers to 6 decimal places.
# -----------------------------------------------------------

from math import sqrt

def distance_between_points(a, b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

# or

from math import hypot

def distance_between_points(a, b):
    return hypot(a.x - b.x, a.y - b.y)

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