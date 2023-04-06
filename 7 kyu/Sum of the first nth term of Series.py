# -----------------------------------------------------------
# Task:
# Your task is to write a function which returns the sum of following series upto nth term(parameter).
# 
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# 
# Rules:
# You need to round the answer to 2 decimal places and return it as String.
# 
# If the given value is 0 then it should return 0.00
# 
# You will only be given Natural Numbers as arguments.
# 
# Examples:(Input --> Output)
# 1 --> 1 --> "1.00"
# 2 --> 1 + 1/4 --> "1.25"
# 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
# -----------------------------------------------------------

def series_sum(n):
    answer = sum(1.0 / (i * 3 + 1) for i in range(n))
    return "%.02f" % answer

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