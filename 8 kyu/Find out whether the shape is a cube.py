# -----------------------------------------------------------
# To find the volume (centimeters cubed) of a cuboid you use the formula:
# 
# volume = Length * Width * Height
# 
# But someone forgot to use proper record keeping, so we only have the volume, and the length of a single side!
# 
# It's up to you to find out whether the cuboid has equal sides (= is a cube).
# 
# Return true if the cuboid could have equal sides, return false otherwise.
# 
# Return false for invalid numbers too (e.g volume or side is less than or equal to 0).
# 
# Note: the sides must be integers
# -----------------------------------------------------------

def cube_checker(volume, side):
    return volume > 0 and side > 0 and (volume % side) % side == 0

# or

def cube_checker(volume, side):
    return 0 < volume == side**3

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