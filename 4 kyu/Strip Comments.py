# -----------------------------------------------------------
# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should 
# also be stripped out.
# 
# Example:
# 
# Given an input string of:
# 
# apples, pears # and bananas
# grapes
# bananas !apples
# 
# The output expected would be:
# 
# apples, pears
# grapes
# bananas
# 
# The code would be called like so:
# 
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"
# -----------------------------------------------------------

def strip_comments(strng, markers):
    arr = strng.split("\n")
    for i in markers:
        arr = [j.split(i)[0].rstrip() for j in arr]
    return "\n".join(arr)

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