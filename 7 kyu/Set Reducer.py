# -----------------------------------------------------------
# Set Reducer
# Intro
# These arrays are too long! Let's reduce them!
# 
# Description
# Write a function that takes in an array of integers from 0-9, and returns a new array:
# 
# Numbers with no identical numbers preceding or following it returns a 1: 2, 4, 9  => 1, 1, 1
# Sequential groups of identical numbers return their count: 6, 6, 6, 6 => 4
# 
# Example
# 
# [0, 4, 6, 8, 8, 8, 5, 5, 7] => [1, 1, 1, 3, 2, 1]
# 
# Your function should then repeat the process on the resulting array, and on the resulting array of that, until it returns a single integer:
# 
# [0, 4, 6, 8, 8, 8, 5, 5, 7] =>  [1, 1, 1, 3, 2, 1] => [3, 1, 1, 1] => [1, 3] => [1, 1] => [2]
# 
# When your function has reduced the array to a single integer following these rules, it should return that integer.
# 
# [2] => 2
# 
# Rules and assertions
# All test arrays will be 2+ in length
# All integers in the test arrays will be positive numbers from 0 - 9
# You should return an integer, not an array with 1 element
# -----------------------------------------------------------

import itertools

def set_reducer(inp):
    while len(inp) > 1:
        inp = [len(list(x2)) for x1, x2 in itertools.groupby(inp)]
    return inp[0]

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