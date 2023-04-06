# -----------------------------------------------------------
# Create a function that finds the integral of the expression passed.
# 
# In order to find the integral all you need to do is add one to the exponent (the second argument), and divide the coefficient (the first argument) 
# by that new number.
# 
# For example for 3x^2, the integral would be 1x^3: we added 1 to the exponent, and divided the coefficient by that new number).
# 
# Notes:
# 
# The output should be a string.
# The coefficient and exponent is always a positive integer.
# 
# Examples
#  3, 2  -->  "1x^3"
# 12, 5  -->  "2x^6"
# 20, 1  -->  "10x^2"
# 40, 3  -->  "10x^4"
# 90, 2  -->  "30x^3"
# -----------------------------------------------------------

def integrate(coefficient, exponent):
    return "{}x^{}".format((coefficient // (exponent + 1)), exponent + 1)

# or

def integrate(coefficient, exponent):
    return f"{coefficient // (exponent + 1)}x^{exponent + 1}"

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