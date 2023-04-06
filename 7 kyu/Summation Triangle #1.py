# -----------------------------------------------------------
# The task
# You have to make a program capable of returning the sum of all the elements of a triangle with side of size n+1n+1n+1.
# 
# The problem
# Your solution has to support 0 <= n≤ <= 10^6 Brute-forcing will not work!
# 
# The definition
# A triangle element aij where i is the column and j is the row can be defined as aij = 2j + i + 1 where 0 <= j <= i <= n
# 
# Examples
# For n = 2:
# 
# 1  2  3      \
#    4  5       \__ 1+2+3+4+5+7 sums to: 22
#       7       /
# sum(2) = 22
# 
# For n = 3:
# 
# 1  2  3  4   \
#    4  5  6    \__ 1+2+3+4+4+5+6+7+8+10 sums to: 50
#       7  8    /
#         10   /
# sum(3) = 50
# 
# Hints
# Euler transform (Optional)
# Sums of powers
# -----------------------------------------------------------

import numpy as np

def get_sum(n):
    n += 1
    x = np.arange(1, n + 1)
    x = x**2 * 2 - x
    return x.sum()

# or

def get_sum(n):
    n += 1
    r = 6
    return (n**2 * 3 + n**3 * (r - 2) - n * (r - 5)) // r

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