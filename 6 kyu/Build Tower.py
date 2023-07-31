# -----------------------------------------------------------
# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" 
# character.
# 
# For example, a tower with 3 floors looks like this:
# 
# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# 
# And a tower with 6 floors looks like this:
# 
# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]
# -----------------------------------------------------------

def tower_builder(n_floors):
    tower = []
    i = 1
    while i <= n_floors:
        empty = " " * (n_floors - i )
        tower.append(empty + "*" + "**" * (i - 1) + empty)
        i += 1
    return tower

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