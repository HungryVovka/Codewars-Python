# -----------------------------------------------------------
# Centered pentagonal number
# Complete the function that takes an integer and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.
# 
# In the image below you can see the first iteration is only a single dot. On the second, there are 6 dots. On the third, there are 16 dots, and on the 
# fourth there are 31 dots. The sequence is: 1, 6, 16, 31...
# 
# If the input is equal to or less than 0, return -1
# 
# Examples
# 1  -->    1
# 2  -->    6
# 8  -->  141
# 0  -->   -1
# 
# Note:
# Input can reach 10**20
# -----------------------------------------------------------

def pentagonal(n):
    return - 1 if n < 1 else 1 + ((n - 1) * 5 * n) // 2

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