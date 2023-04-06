# -----------------------------------------------------------
# In your class, you have started lessons about geometric progression. Since you are also a programmer, you have decided to write a function that will 
# print first n elements of the sequence with the given constant r and first element a.
# 
# Result should be separated by comma and space.
# 
# Example
# geometric_sequence_elements(2, 3, 5) == '2, 6, 18, 54, 162'
# 
# More info: https://en.wikipedia.org/wiki/Geometric_progression
# -----------------------------------------------------------

def geometric_sequence_elements(a, r, n):
    arr = [str(a)]
    i = 1
    while i < n:
        a *= r
        arr.append(str(a))
        i += 1
    return ", ".join(arr)

# or

def geometric_sequence_elements(a, r, n):
    arr = []
    for i in range(n):
        arr.append(str(a))
        a *= r
    return ", ".join(arr)

# or

def geometric_sequence_elements(a, r, n):
    arr = [str(a * r**i) for i in range(n)]
    return ", ".join(arr)

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