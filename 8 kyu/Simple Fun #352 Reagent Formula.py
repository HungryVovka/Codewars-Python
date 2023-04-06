# -----------------------------------------------------------
# Now we will confect a reagent. There are eight materials to choose from, numbered 1,2,..., 8 respectively.
# 
# We know the rules of confect:
# 
# material1 and material2 cannot be selected at the same time
# material3 and material4 cannot be selected at the same time
# material5 and material6 must be selected at the same time
# material7 or  material8 must be selected(at least one, or both)
# 
# Task
# You are given a integer array formula. Array contains only digits 1-8 that represents material 1-8. Your task is to determine if the formula is valid. 
# Returns true if it's valid, false otherwise.
# 
# Example
# For formula = [1,3,7], The output should be true.
# 
# For formula = [7,1,2,3], The output should be false.
# 
# For formula = [1,3,5,7], The output should be false.
# 
# For formula = [1,5,6,7,3], The output should be true.
# 
# For formula = [5,6,7], The output should be true.
# 
# For formula = [5,6,7,8], The output should be true.
# 
# For formula = [6,7,8], The output should be false.
# 
# For formula = [7,8], The output should be true.
# 
# Note
# All inputs are valid. Array contains at least 1 digit. Each digit appears at most once.
# 
# Happy Coding ^_^
# -----------------------------------------------------------

def isValid(rf):
    if 1 in rf and 2 in rf: return False
    if 3 in rf and 4 in rf: return False
    if 5 in rf and 6 not in rf: return False
    if 6 in rf and 5 not in rf: return False
    if 7 not in rf and 8 not in rf: return False
    return True

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