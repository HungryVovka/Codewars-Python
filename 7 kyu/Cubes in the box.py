# -----------------------------------------------------------
# Cubes in the box
# Your job is to write a function f(x,y,z) to count how many cubes of any size can fit inside a x*y*z box. For example, a 2*2*3 box has 12 1*1*1 
# cubes, 2 2*2*2 cubes, so a total of 14 cubes in the end. See the animation below for a visual description of the task!
# 
# Notes:
# x,y,z are strictly positive and will not be too big.
# -----------------------------------------------------------

def f(x, y, z):
    x += 1; y += 1; z += 1
    a = min(x, y, z)
    b = a * (a + 1) / 2
    c = b * (a * 2 + 1) / 3
    cube = b * b
    answer = a * x * y * z\
            + (x + y + z) * c\
            - (x * y + x * z + y * z) * b\
            - cube
    return answer

# or

def f(x, y, z):
    answer = 0
    while min(x, y, z) > 0:
        answer += x * y * z;
        x -= 1; y -= 1; z -= 1
    return answer

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