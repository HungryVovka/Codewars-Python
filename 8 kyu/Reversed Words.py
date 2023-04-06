# -----------------------------------------------------------
# Complete the solution so that it reverses all of the words within the string passed in.
# 
# Example(Input --> Output):
# 
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
# -----------------------------------------------------------

def reverse_words(s):
    s = s.split()
    s.reverse()
    s = " ".join(s)
    return s

# or

def reverse_words(s):
    separator = " "
    return separator.join(reversed(s.split(separator)))

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