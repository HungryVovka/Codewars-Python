# -----------------------------------------------------------
# Colour plays an important role in our lifes. Most of us like this colour better then another. User experience specialists believe that certain colours 
# have certain psychological meanings for us.
# 
# You are given a 2D array, composed of a colour and its 'common' association in each array element. The function you will write needs to return the 
# colour as 'key' and association as its 'value'.
# 
# For example:
# 
# var array = [["white", "goodness"], ...] returns [{'white': 'goodness'}, ...]
# -----------------------------------------------------------

def colour_association(arr):
    association = []
    for i in arr:
        colour = {}
        colour[i[0]] = i[1]
        association.append(colour)
    return association

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