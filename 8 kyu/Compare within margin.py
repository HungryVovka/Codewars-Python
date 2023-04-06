# -----------------------------------------------------------
# Create a function close_compare that accepts 3 parameters: a, b, and an optional margin. The function should return whether a is lower than, 
# close to, or higher than b.
# 
# a is considered "close to" b if margin is greater than or equal to the distance between a and b.
# 
# Please note the following:
# 
# When a is close to b, return 0.
# Otherwise...
# 
# When a is less than b, return -1.
# 
# When a is greater than b, return 1.
# 
# If margin is not given, treat it as zero.
# 
# Assume: margin >= 0
# 
# Tip: Some languages have a way to make parameters optional.
# 
# Example 1
# If a = 3, b = 5, and margin = 3, then close_compare(a, b, margin) should return 0.
# 
# This is because a and b are no more than 3 numbers apart.
# 
# Example 2
# If a = 3, b = 5, and margin = 0, then close_compare(a, b, margin) should return -1.
# 
# This is because the distance between a and b is greater than 0, and a is less than b.
# -----------------------------------------------------------

def close_compare(a, b, margin = 0):
    if a == b or margin >= abs(a - b):
        return 0
    elif a < b:
        return -1
    elif a > b:
        return 1

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