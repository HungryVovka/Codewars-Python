# -----------------------------------------------------------
# Build a function that returns an array of integers from n to 1 where n>0.
# 
# Example : n=5 --> [5,4,3,2,1]
# -----------------------------------------------------------

def reverse_seq(n):
    n_arr = []
    p = n
    while p > 0:
        n_arr.append(p)
        p -= 1
    return(n_arr)

# or

def reverse_seq(n):
    return [i for i in range(n, 0, -1)]

# or

def reverse_seq(n):
    return list(range(n, 0, -1))

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