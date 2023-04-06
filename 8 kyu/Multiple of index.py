# -----------------------------------------------------------
# Return a new array consisting of elements which are multiple of their own index in input array (length > 1).
# 
# Some cases:
# [22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]
# 
# [68, -1, 1, -7, 10, 10] => [-1, 10]
# 
# [-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]
# -----------------------------------------------------------

def multiple_of_index(arr):
    new_arr = []
    for i in range(1, len(arr)):
        if arr[i] % i == 0:
            new_arr.append(arr[i])
    return new_arr

# or

def multiple_of_index(arr):
    return list(arr[i] for i in range(1, len(arr)) if arr[i] % i == 0)

# or

def multiple_of_index(arr):
    return [j for i, j in enumerate(arr) if i and j % i == 0]

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