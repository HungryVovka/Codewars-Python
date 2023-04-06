# -----------------------------------------------------------
# Write a function to get the first element(s) of a sequence. Passing a parameter n (default=1) will return the first n element(s) of the sequence.
# 
# If n == 0 return an empty sequence []
# 
# Examples
# arr = ['a', 'b', 'c', 'd', 'e']
# first(arr)    # --> ['a']
# first(arr, 2) # --> ['a', 'b']
# first(arr, 3) # --> ['a', 'b', 'c']
# first(arr, 0) # --> []
# -----------------------------------------------------------

def first(seq, n = 1):
    return [j for i, j in enumerate(seq) if i < n]

# or

def first(seq, n = 1):
    return seq[:n]

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