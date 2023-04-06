# -----------------------------------------------------------
# In this Kata you must calulate the number of bounces a ball makes when shot between two walls
# 
# Task Details:
# Mr Reecey has bought a new ball cannon and he lives in a tower block
# 
# He wants to calulate the number of bounces between the two towers before he shoots his shot
# 
# The gun is set up to fire with a velocity v, on the tower block height h and the width between them as w
# 
# The gun is set up parrallel to the horizontal
# 
# In this diagram the ball bounces twice:
# 
#         |                Velocity      |    / \
#         |                     <---_____|     |
#         |                    *    ______     |
#         |             *                |     |
#         |                              |     |
#         |        *                     |     |
#         |                              |     |
#         |                              |     |
#         |   *                          |     |
#         |                              |     |
#         |*                             |     |
#         |                              |   Height
#         |         *                    |     |
#         |                              |     |
#         |                              |     |
#         |               *              |     |
#         |                              |     |
#         |                              |     |
#         |                     *        |     |
#         |                              |     |
#         |                              |     |
#         |                          *   |     |
#         |                              |     |
#         |                             *|     |                                               
#         <-------- Width -------------->     \ /
# 
# Technicalities:
# There are 5 fixed tests and 100 random tests
# 
# SI units are used for height, width and velocity (m,m m/s)
# 
# Mr Reecey uses g = 9.81, ignores air resistance and assumes elastic collisions
# 
# The ball is modlled as very small
# 
# Also, remember to return the number of bounces as an integer
# -----------------------------------------------------------

import math

def bounce_count(height, width, velocity):
    g = 9.81
    bounce = 0
    time = math.sqrt(height * 2 / g)
    i = time * velocity
    while i > width:
        bounce += 1
        i -= width
    return bounce

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