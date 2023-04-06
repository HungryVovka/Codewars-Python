# -----------------------------------------------------------
# One of the common ways of representing color is the RGB color model, in which the Red, Green, and Blue primary colors of light are added together 
# in various ways to reproduce a broad array of colors.
# 
# One of the ways to determine brightness of a color is to find the value V of the alternative HSV (Hue, Saturation, Value) color model. Value is defined 
# as the largest component of a color:
# 
# V = max(R,G,B)
# 
# You are given a list of colors in 6-digit hexidecimal notation #RRGGBB. Return the brightest of these colors!
# 
# For example,
# 
# brightest(["#001000", "#000000"]) == "#001000"
# brightest(["#ABCDEF", "#123456"]) == "#ABCDEF"
# 
# If there are multiple brightest colors, return the first one:
# 
# brightest(["#00FF00", "#FFFF00", "#01130F"]) == "#00FF00"
# 
# Note that both input and output should use upper case for characters A, B, C, D, E, F.
# -----------------------------------------------------------

def brightest(colors):
    bright = []
    for i in colors:
        bright.append(max(i[1:3], i[3:5], i[5:7]))
    return colors[bright.index(max(bright))]

# or

def brightest(colors):
    return max(colors, key = lambda x: max(x[1:3], x[3:5], x[5:]))

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