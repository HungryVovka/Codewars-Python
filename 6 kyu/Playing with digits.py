# -----------------------------------------------------------
# Some numbers have funny properties. For example:
# 
# 89 --> 8¹ + 9² = 89 * 1
# 
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# 
# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
# 
# we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
# 
# In other words:
# 
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# 
# If it is the case we will return k, if not return -1.
# 
# Note: n and p will always be given as strictly positive integers.
# 
# dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
# dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
# dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
# dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# -----------------------------------------------------------

def dig_pow(n, p):
    arr = list(str(n))
    arr_pow_sum = 0
    for i in arr:
        arr_pow_sum += int(i)**p
        p += 1
    k = arr_pow_sum / n
    return -1 if k % 1 != 0 else k

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