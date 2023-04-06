# -----------------------------------------------------------
# SpeedCode #2 - Array Madness
# 
# Objective
# Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly 
# greater than the sum of the cubes of each element in b.
# 
# E.g.
# 
# array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3
# 
# Get your timer out. Are you ready? Ready, get set, GO!!!
# -----------------------------------------------------------

def array_madness(a,b):
    return sum(map(lambda a: a * a, a)) > sum(map(lambda b: b * b * b, b))

# or

def array_madness(a,b):
    return sum(i**2 for i in a) > sum(j**3 for j in b)

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