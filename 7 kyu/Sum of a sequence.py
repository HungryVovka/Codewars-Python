# -----------------------------------------------------------
# Your task is to write a function which returns the sum of a sequence of integers.
# 
# The sequence is defined by 3 non-negative values: begin, end, step.
# 
# If begin value is greater than the end, your function should return 0. If end is not the result of an integer number of steps, then don't add it to the 
# sum. See the 4th example below.
# 
# Examples
# 
# 2,2,2 --> 2
# 2,6,2 --> 12 (2 + 4 + 6)
# 1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
# 1,5,3  --> 5 (1 + 4)
# -----------------------------------------------------------

def sequence_sum(begin_number, end_number, step):
    answer = 0
    if begin_number > end_number:
        return answer
    while begin_number <= end_number:
        answer += begin_number
        begin_number += step
    return answer

# or

def sequence_sum(begin_number, end_number, step):
    answer = 0
    if begin_number > end_number:
        return answer
    i = (end_number - begin_number) // step
    answer = (i + 1) * (begin_number + step * i / 2)
    return answer

# or

def sequence_sum(begin_number, end_number, step):
    answer = 0
    if begin_number > end_number:
        return answer
    answer = sum(range(begin_number, end_number + 1, step))
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