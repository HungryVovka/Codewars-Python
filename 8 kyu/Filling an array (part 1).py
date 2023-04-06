# -----------------------------------------------------------
# We want an array, but not just any old array, an array with contents!
# 
# Write a function that produces an array with the numbers 0 to N-1 in it.
# 
# For example, the following code will result in an array containing the numbers 0 to 4:
# 
# arr(5) // => [0,1,2,3,4]
# 
# Note: The parameter is optional. So you have to give it a default value.
# -----------------------------------------------------------

def arr(n = 0):
    return [i for i in range(n)]

# or

def arr(n = 0):
    return list(range(n))

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