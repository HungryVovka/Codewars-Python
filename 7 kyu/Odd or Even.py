# -----------------------------------------------------------
# Task:
# Given a list of integers, determine whether the sum of its elements is odd or even.
# 
# Give your answer as a string matching "odd" or "even".
# 
# If the input array is empty consider it as: [0] (array with a zero).
# 
# Examples:
# Input: [0]
# Output: "even"
# 
# Input: [0, 1, 4]
# Output: "odd"
# 
# Input: [0, -1, -5]
# Output: "even"
# 
# Have fun!
# -----------------------------------------------------------

def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return("even")
    if sum(arr) % 2 == 1:
        return("odd")

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