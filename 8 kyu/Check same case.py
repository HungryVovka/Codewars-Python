# -----------------------------------------------------------
# Write a function that will check if two given characters are the same case.
# 
# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0
# 
# Examples
# 'a' and 'g' returns 1
# 
# 'A' and 'C' returns 1
# 
# 'b' and 'G' returns 0
# 
# 'B' and 'g' returns 0
# 
# '0' and '?' returns -1
# -----------------------------------------------------------

cap_let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low_let = []
for c in cap_let:
    low_let.append(c.lower())

def same_case(a, b):
    if a in cap_let and b in cap_let:
        return(1)
    if a in low_let and b in low_let:
        return(1)
    if (a in cap_let and b in low_let) or (a in low_let and b in cap_let):
        return(0)
    if (a not in cap_let and a not in low_let) or (b not in cap_let and b not in low_let):
        return(-1)

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