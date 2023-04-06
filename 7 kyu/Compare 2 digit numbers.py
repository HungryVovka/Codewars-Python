# -----------------------------------------------------------
# You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers, and return the result in %.
# 
# Example:
# 
# compare(13,14)=50%;
# compare(23,22)=50%;
# compare(15,51)=100%;
# compare(12,34)=0%.
# -----------------------------------------------------------

def compare(a, b):
    a = sorted(list(str(a)))
    b = sorted(list(str(b)))
    if a == b:
        return "100%"
    elif a[0] in b or a[1] in b:
        return "50%"
    else:
        return "0%"

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