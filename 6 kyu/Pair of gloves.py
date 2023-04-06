# -----------------------------------------------------------
# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from 
# the gloves you have in your drawer.
# 
# Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can 
# form pairs.
# 
# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)
# 
# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)
# -----------------------------------------------------------

import collections

def number_of_pairs(gloves):
    pair = collections.defaultdict(int)
    for glov in gloves:
        pair[glov] += 1
    pair = sum(i // 2 for i in pair.values())
    return pair

# or

def number_of_pairs(gloves):
    glov = {}
    for i in gloves:
        if i in glov:
            glov[i] += 1
        else:
            glov[i] = 1
    pair = 0
    for j in glov.values():
        if j > 1:
            pair += j // 2
    return pair

# or

def number_of_pairs(gloves):
    return sum(gloves.count(i) // 2 for i in set(gloves))

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