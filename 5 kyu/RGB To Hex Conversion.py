# -----------------------------------------------------------
# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid 
# decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
# 
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
# 
# The following are examples of expected output values:
# 
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3
# -----------------------------------------------------------

def rgb(r, g, b):
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    return ("%02x%02x%02x" % (r, g, b)).upper()

# or

def rgb(r, g, b):
    proper = lambda x: max(0, min(x, 255))
    return ("%02x%02x%02x" % (proper(r), proper(g), proper(b))).upper()

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