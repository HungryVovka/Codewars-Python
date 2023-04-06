# -----------------------------------------------------------
# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and 
# false in any other case.
# 
# (In this case, all triangles must have surface greater than 0 to be accepted).
# -----------------------------------------------------------

def is_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

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