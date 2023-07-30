# -----------------------------------------------------------
# Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to 
# longest.
# 
# For example, if this array were passed as an argument:
# 
# ["Telescopes", "Glasses", "Eyes", "Monocles"]
# 
# Your function would return the following array:
# 
# ["Eyes", "Glasses", "Monocles", "Telescopes"]
# 
# All of the strings in the array passed to your function will be different lengths, so you will not have to decide how to order multiple strings of the 
# same length.
# -----------------------------------------------------------

def sort_by_length(arr):
    arr.sort(key = len)
    return arr

# or

def sort_by_length(arr):
    return sorted(arr, key = len)

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