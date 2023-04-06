# -----------------------------------------------------------
# Scenario
# Several people are standing in a row divided into two teams.
# The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.
# 
# Task
# Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, where the first one is the total weight of 
# team 1, and the second one is the total weight of team 2.
# 
# Notes
# Array size is at least 1.
# All numbers will be positive.
# 
# Input >> Output Examples
# rowWeights([13, 27, 49])  ==>  return (62, 27)
# 
# Explanation:
# The first element 62 is the total weight of team 1, and the second element 27 is the total weight of team 2.
# 
# rowWeights([50, 60, 70, 80])  ==>  return (120, 140)
# 
# Explanation:
# The first element 120 is the total weight of team 1, and the second element 140 is the total weight of team 2.
# 
# rowWeights([80])  ==>  return (80, 0)
# 
# Explanation:
# The first element 80 is the total weight of team 1, and the second element 0 is the total weight of team 2.
# -----------------------------------------------------------

def row_weights(array):
    team1 = 0
    team2 = 0
    for i, j in enumerate(array):
        if i % 2 == 0:
            team1 += j
        else:
            team2 += j
    return (team1, team2)

# or

def row_weights(array):
    return (sum(array[0::2]), sum(array[1::2]))

# or

def row_weights(array):
    return (sum(array[::2]), sum(array[1::2]))

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