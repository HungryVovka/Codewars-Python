# -----------------------------------------------------------
# Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an 
# empty array.
# 
# For example:
# 
# solution([1, 2, 10, 50, 5]); // should return [1,2,5,10,50]
# solution(null); // should return []
# -----------------------------------------------------------

def solution(nums):
    if nums != None:
        nums.sort()
        return(nums)
    else:
        return([])

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