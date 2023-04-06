# -----------------------------------------------------------
# You get an array of numbers, return the sum of all of the positives ones.
# 
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# 
# Note: if there is nothing to sum, the sum is default to 0.
# -----------------------------------------------------------

def positive_sum(arr):
    pos = []
    for a in arr:
        if a > 0:
            pos.append(a)
    return sum(pos)

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