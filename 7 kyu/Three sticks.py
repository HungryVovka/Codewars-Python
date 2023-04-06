# -----------------------------------------------------------
# Imagine that you are given two sticks. You want to end up with three sticks of equal length. You are allowed to cut either or both of the sticks to 
# accomplish this, and can throw away leftover pieces.
# 
# Write a function, maxlen, that takes the lengths of the two sticks (L1 and L2, both positive values), that will return the maximum length you can make 
# the three sticks.
# -----------------------------------------------------------

def maxlen(L1,L2):
    return L1 / 3 if L1 / 3 > L2 and L1 > L2 else \
        L2 / 3 if L2 / 3 > L1 and L1 < L2 else \
        L1 if L2 / 2 > L1 and L1 < L2 else \
        L2 if L1 / 2 > L2 and L1 > L2 else \
        L1 / 2 if L1 / 2 < L2 and L1 > L2 else \
        L2 / 2 if L2 / 2 < L1 and L1 < L2 else 0

# or

def maxlen(L1, L2):
    x1, x2 = sorted((L1, L2))
    return min(x2 / 2, max(x2 / 3, x1))

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