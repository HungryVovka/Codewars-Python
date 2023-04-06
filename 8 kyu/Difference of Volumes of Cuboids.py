# -----------------------------------------------------------
# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, 
# representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.
# 
# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function 
# should return 8.
# 
# Your function will be tested with pre-made examples as well as random ones.
# 
# If you can, try writing it in one line of code.
# -----------------------------------------------------------

from functools import reduce
from operator import mul

def find_difference(a, b):
    return abs(reduce(mul, a) - reduce(mul, b))

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