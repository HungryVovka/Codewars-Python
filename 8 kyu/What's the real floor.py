# -----------------------------------------------------------
# Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor (due to superstition).
# 
# Write a function that given a floor in the american system returns the floor in the european system.
# 
# With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 
# 13, they move down by two because there are two omitted numbers below them.
# 
# Basements (negatives) stay the same as the universal level.
# 
# More information here
# 
# Examples
# 1  =>  0 
# 0  =>  0
# 5  =>  4
# 15  =>  13
# -3  =>  -3
# -----------------------------------------------------------

def get_real_floor(n):
    if n < 1:
        return n
    elif n <= 13:
        return n - 1
    else:
        return n - 2

# or

def get_real_floor(n):
    return n - 2 if n > 13 else n - 1 if n > 0 else n

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