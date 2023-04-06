# -----------------------------------------------------------
# The museum of incredible dull things
# The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect, comes up with a plan to remove the most 
# boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.
# 
# However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the 
# items after one removed the lowest one. Fair enough.
# 
# Task
# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, 
# remove the one with a lower index. If you get an empty array/list, return an empty array/list.
# 
# Don't change the order of the elements that are left.
# 
# Examples
# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]
# -----------------------------------------------------------

def remove_smallest(numbers):
    if len(numbers) == 0:
        return numbers
    i = numbers.index(min(numbers))
    return numbers[0:i] + numbers[i + 1:]

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