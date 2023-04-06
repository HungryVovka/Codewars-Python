# -----------------------------------------------------------
# My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!
# 
# In honor of my grandfather's memory we will write a function using his formula!
# 
# Take a list of ages when each of your great-grandparent died.
# Multiply each number by itself.
# Add them all together.
# Take the square root of the result.
# Divide by two.
# 
# Example
# predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
# 
# Note: the result should be rounded down to the nearest integer.
# 
# Some random tests might fail due to a bug in the JavaScript implementation. Simply resubmit if that happens to you.
# -----------------------------------------------------------

import math

def predict_age(age1, age2, age3, age4, age5, age6, age7, age8):
    arr = [age1, age2, age3, age4, age5, age6, age7, age8]
    answer = math.sqrt(sum(i**2 for i in arr)) / 2
    return math.floor(answer)

# or

import math

def predict_age(*args):
    arr = [i for i in args]
    answer = math.sqrt(sum(j**2 for j in arr)) * 0.5
    return math.floor(answer)

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