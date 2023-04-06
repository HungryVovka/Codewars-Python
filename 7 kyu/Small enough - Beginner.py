# -----------------------------------------------------------
# You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return 
# true. Else, return false.
# 
# You can assume all values in the array are numbers.
# -----------------------------------------------------------

def small_enough(array, limit):
    return all(a <= limit for a in array)

# or

def small_enough(array, limit):
    return max(array) <= limit

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