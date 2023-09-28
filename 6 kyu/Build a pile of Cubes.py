# -----------------------------------------------------------
# Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume 
# of (n - 1)^3  and so on until the top which will have a volume of 1^3.
# 
# You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?
# 
# The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m and you have to return the integer n such as n^3 + 
# (n - 1)^3 + (n - 2)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.
# 
# Examples:
# findNb(1071225) --> 45
# 
# findNb(91716553919377) --> -1
# -----------------------------------------------------------

def find_nb(m):
    n, volume = 0, 0
    while volume < m:
        n += 1
        volume += n**3
    return n if volume == m else -1

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