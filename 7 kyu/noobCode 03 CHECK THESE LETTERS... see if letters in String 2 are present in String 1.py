# -----------------------------------------------------------
# Write a function that checks if all the letters in the second string are present in the first one at least once, regardless of how many times they appear:
# 
# ["ab", "aaa"]    =>  true
# ["trances", "nectar"]    =>  true
# ["compadres", "DRAPES"]  =>  true
# ["parses", "parsecs"]    =>  false
# 
# Function should not be case sensitive, as indicated in example #2. Note: both strings are presented as a single argument in the form of an array.
# -----------------------------------------------------------

def letter_check(arr):
    a = set(arr[0].lower())
    b = set(arr[1].lower())
    return b <= a

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