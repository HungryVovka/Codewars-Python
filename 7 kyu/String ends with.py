# -----------------------------------------------------------
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
# 
# Examples:
# 
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
# -----------------------------------------------------------

def solution(string, ending):
    if string.endswith(ending):
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