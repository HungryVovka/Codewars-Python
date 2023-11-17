# -----------------------------------------------------------
# My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published 
# and each month he is the last on the list which means he is the heaviest.
# 
# I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to 
# numbers. The weight of a number will be from now on the sum of its digits.
# 
# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.
# 
# Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?
# 
# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 
# 
# "100 180 90 56 65 74 68 86 99"
# 
# When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:
# 
# 180 is before 90 since, having the same "weight" (9), it comes before as a string.
# 
# All numbers in the list are positive numbers and the list can be empty.
# 
# Notes
# it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
# For C: The result is freed.
# -----------------------------------------------------------

weights = lambda arr: (sum(int(i) for i in arr), arr)

def order_weight(strng):
    return " ".join(sorted(strng.split(), key=weights))

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