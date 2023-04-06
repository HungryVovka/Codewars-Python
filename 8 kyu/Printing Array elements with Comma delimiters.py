# -----------------------------------------------------------
# Input: Array of elements
# 
# ["h","o","l","a"]
# 
# Output: String with comma delimited elements of the array in th same order.
# 
# "h,o,l,a"
# 
# Note: if this seems too simple for you try the next level
# -----------------------------------------------------------

def print_array(arr):
    answer = []
    for i in arr:
        answer.append(str(i))
    return ",".join(answer)

# or

def print_array(arr):
    return ",".join(str(i) for i in arr)

# or

def print_array(arr):
    return ",".join(map(str, arr))

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