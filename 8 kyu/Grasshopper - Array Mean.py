# -----------------------------------------------------------
# Find Mean
# Find the mean (average) of a list of numbers in an array.
# 
# Information
# To find the mean (average) of a set of numbers add all of the numbers together and divide by the number of values in the list.
# 
# For an example list of 1, 3, 5, 7
# 
# 1. Add all of the numbers
# 
# 1+3+5+7 = 16
# 
# 2. Divide by the number of values in the list. In this example there are 4 numbers in the list.
# 
# 16/4 = 4
# 
# 3. The mean (or average) of this list is 4
# -----------------------------------------------------------

def find_average(nums):
    try:
        return sum(nums) / len(nums)
    except (ZeroDivisionError):
        return 0

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