# -----------------------------------------------------------
# Complete the function that returns an array of length n, starting with the given number x and the squares of the previous number. If n is negative 
# or zero, return an empty array/list.
# 
# Examples
# 2, 5  -->  [2, 4, 16, 256, 65536]
# 3, 3  -->  [3, 9, 81]
# -----------------------------------------------------------

def squares(x, n):
    i = 1
    arr = []
    while i <= n:
        arr.append(x)
        x = x**2
        i += 1
    return arr

# or

def squares(x, n):
    return list(x**(2**i) for i in range(n))

# or

squares = lambda x, y : [x**(2**y1) for y1 in range(y)]

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