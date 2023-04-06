# -----------------------------------------------------------
# Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
# 
# Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.
# 
# Examples
#  123 ->  321
# -456 -> -654
# 1000 ->    1
# -----------------------------------------------------------

def reverse_number(n):
    if n >= 0:
        n = str(n)
        return int(n[::-1])
    if n < 0:
        n = str(abs(n))
        return 0 - int(n[::-1])

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