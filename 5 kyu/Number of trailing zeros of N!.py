# -----------------------------------------------------------
# Write a program that will calculate the number of trailing zeros in a factorial of a given number.
# 
# N! = 1 * 2 * 3 *  ... * N
# 
# Be careful 1000! has 2568 digits...
# 
# For more info, see: http://mathworld.wolfram.com/Factorial.html
# 
# Examples
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
# 
# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros
# 
# Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
# -----------------------------------------------------------

def zeros(n):
    trailing_zeroes = 0
    check_zero = 5
    while n / check_zero >= 1.0:
        trailing_zeroes += n // check_zero
        check_zero *= 5
    return trailing_zeroes

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