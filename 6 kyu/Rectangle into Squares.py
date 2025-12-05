# -----------------------------------------------------------
# The drawing below gives an idea of how to cut a given "true" rectangle into 
# squares ("true" rectangle meaning that the two dimensions are different).
# 
# +-------+-------+-------+-------+-------+
# |       |       |       |       |       |
# |   R   |   R   |   R   |   G   |   G   |
# |       |       |  3²=9 |       |       |
# +-------+-------+-------+-------+-------+
# |       |       |       |       |       |
# |   R   |   R   |   R   |   G   |   G   |
# |       |       |       |  2²=4 |       |
# +-------+-------+-------+-------+-------+
# |       |       |       |       |       |
# |   R   |   R   |   R   |   B   |   P   |
# |       |       |       |   1   |   1   |
# +-------+-------+-------+-------+-------+
# 
# Can you translate this drawing into an algorithm?
# 
# You will be given two dimensions
# 
# a positive integer length
# a positive integer width
# 
# You will return a collection or a string (depending on the language; Shell bash, 
# PowerShell, Pascal and Fortran return a string) with the size of each of the 
# squares.
# 
# Examples in general form:
# (depending on the language)
# 
#   sqInRect(5, 3) should return [3, 2, 1, 1]
#   sqInRect(3, 5) should return [3, 2, 1, 1]
#   
#   You can see examples for your language in **"SAMPLE TESTS".**
# 
# Notes:
# lng == wdth as a starting case would be an entirely different problem and 
# the drawing is planned to be interpreted with lng != wdth. (See kata, Square into 
# Squares. Protect trees! http://www.codewars.com/kata/54eb33e5bc1a25440d000891 for this 
# problem).
# 
# When the initial parameters are so that lng == wdth, the solution [lng] 
# would be the most obvious but not in the spirit of this kata so, in that case, 
# return None/nil/null/Nothing or return {} with C++, [] with Perl, 
# Raku.
# 
# In that case the returned structure of C will have its sz component equal 
# to 0.
# 
# Return the string "nil" with Bash, PowerShell, Pascal and Fortran.
# -----------------------------------------------------------

def sq_in_rect(length: int, width: int) -> list[int] | None:
    if length == width:
        return None
    answer: list[int] = []
    longer_side = max(length, width)
    shorter_side = min(length, width)
    while longer_side > 0 and shorter_side > 0:
        answer.append(shorter_side)
        longer_side -= shorter_side
        if longer_side < shorter_side:
            longer_side, shorter_side = shorter_side, longer_side
    return answer

# -----------------------------------------------------------
# License
# Tasks are the property of Codewars (https://www.codewars.com/) 
# and users of this resource.
# 
# All solution code in this repository 
# is the personal property of Vladimir Rukavishnikov
# (vladimirrukavishnikovmail@gmail.com).
# 
# Copyright (C) 2025 Vladimir Rukavishnikov
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