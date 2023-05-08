# -----------------------------------------------------------
# N:
# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# 
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# 
# It’s guaranteed that array contains at least 3 numbers.
# 
# The tests contain some very huge arrays, so think about performance.
# -----------------------------------------------------------

def find_uniq(arr):
    arr = sorted(arr)
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]

# or

def find_uniq(arr):
    a, b = set(arr)
    if arr.count(a) < 2:
        return a
    else:
        return b

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