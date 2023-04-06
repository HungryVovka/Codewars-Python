# -----------------------------------------------------------
# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that 
# contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
# 
# Example: (Input --> Output)
# 
# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)
# -----------------------------------------------------------

def is_isogram(string):
    s = string.lower()
    if len(set(s)) == len(s) or len(s) == 0:
        return True
    else:
        return False

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