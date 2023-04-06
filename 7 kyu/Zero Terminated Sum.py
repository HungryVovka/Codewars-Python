# -----------------------------------------------------------
# This kata is part of the collection Mary's Puzzle Books.
# 
# Zero Terminated Sum
# Mary has another puzzle book, and it's up to you to help her out! This book is filled with zero-terminated substrings, and you have to find the 
# substring with the largest sum of its digits. For example, one puzzle looks like this:
# 
# "72102450111111090"
# 
# Here, there are 4 different substrings: 721, 245, 111111, and 9. The sums of their digits are 10, 11, 6, and 9 respectively. Therefore, the 
# substring with the largest sum of its digits is 245, and its sum is 11.
# 
# Write a function largest_sum which takes a string and returns the maximum of the sums of the substrings. In the example above, your function 
# should return 11.
# 
# Notes:
# A substring can have length 0. For example, 123004560 has three substrings, and the middle one has length 0.
# All inputs will be valid strings of digits, and the last digit will always be 0.
# -----------------------------------------------------------

def largest_sum(s):
    s = s.split("0")
    arr = []
    for i in s:
        arr.append(sum(int(j) for j in i))
    return max(arr)

# or

def largest_sum(s):
    s = s.split("0")
    arr = []
    for i in s:
        arr.append(sum(map(int, i)))
    return max(arr)

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