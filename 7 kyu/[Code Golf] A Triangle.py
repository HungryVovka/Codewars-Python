# -----------------------------------------------------------
# Task
# Given three sides a, b and c, determine if a triangle can be built out of them.
# 
# Code limit
# Your code can be up to 40 characters long.
# 
# Note
# Degenerate triangles are not valid in this kata.
# -----------------------------------------------------------

triangle=lambda a,b,c:a+b>c>abs(b-a)

# or

triangle=lambda *x:sum(x)>2*max(x)

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