# -----------------------------------------------------------
# Task
# Given a Divisor and a Bound , Find the largest integer N , Such That ,
# 
# Conditions :
# N is divisible by divisor
# 
# N is less than or equal to bound
# 
# N is greater than 0.
# 
# Notes
# The parameters (divisor, bound) passed to the function are only positive values .
# It's guaranteed that a divisor is Found .
# 
# Input >> Output Examples
# maxMultiple (2,7) ==> return (6)
# 
# Explanation:
# (6) is divisible by (2) , (6) is less than or equal to bound (7) , and (6) is > 0 .
# 
# maxMultiple (10,50)  ==> return (50)
# 
# Explanation:
# (50) is divisible by (10) , (50) is less than or equal to bound (50) , and (50) is > 0 .*
# 
# maxMultiple (37,200) ==> return (185)
# 
# Explanation:
# (185) is divisible by (37) , (185) is less than or equal to bound (200) , and (185) is > 0 .
# -----------------------------------------------------------

def max_multiple(divisor, bound):
    return bound - (bound % divisor)

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