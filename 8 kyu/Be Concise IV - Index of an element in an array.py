# -----------------------------------------------------------
# Be Concise IV - Index of an element in an array
# 
# Task
# Provided is a function find which accepts two parameters in the following order: array, element and returns the index of the element if found 
# and "Not found" otherwise. Your task is to shorten the code as much as possible in order to meet the strict character count requirements of the 
# Kata. (no more than 85) You may assume that all array elements are unique.
# -----------------------------------------------------------

def find(y, x):
    return y.index(x) if x in y else "Not found"

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