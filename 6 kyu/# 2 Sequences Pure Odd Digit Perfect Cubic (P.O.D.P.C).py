# -----------------------------------------------------------
# The number 1331 is the first positive perfect cube, higher than 1, having all its digits odd (its cubic root is 11).
# 
# The next one is 3375.
# 
# In the interval [-5000, 5000] there are six pure odd digit perfect cubic numbers and are: [-3375,-1331, -1, 1, 1331, 3375]
# 
# Give the numbers of this sequence that are in the range [a,b] (both values inclusive)
# 
# Examples:
# 
# odd_dig_cubic(-5000, 5000) == [-3375,-1331, -1, 1, 1331, 3375] # the output should be sorted.
# odd_dig_cubic(0, 5000) == [1, 1331, 3375]
# odd_dig_cubic(-1, 5000) == [-1, 1, 1331, 3375]
# odd_dig_cubic(-5000, -2) == [-3375,-1331]
# 
# Features of the random tests for python:
# 
# number of Tests = 94
# minimum value for a = -1e17
# maximum value for b = 1e17
# 
# You do not have to check the entries, a and b always integers and a < b
# 
# Working well in Python 2 and Python 3. Translation into Ruby is coming soon.
# -----------------------------------------------------------

pos_perfect_cubes = [
    1,
    1331,
    3375,
    35937,
    59319,
    357911,
    753571,
    5177717,
    5359375,
    5735339,
    9393931,
    17373979,
    37595375,
    37159393753,
    99317171591,
    175333911173,
    397551775977,
    1913551573375,
    9735913353977,
    11997979755957,
    17171515157399,
    335571975137771,
    1331399339931331,
    1951953359359375,
    7979737131773191,
    11751737113715977,
    13337513771953951,
    99133919737193375,
    119397111955573375,
    355519351557373375,
    1331119793593735937,
    13715335571137177375,
    17997313379731159131,
    131755133155395759157,
    197993713715333373375,
    373935353339777579713,
    575999939313173595375,
    1391579155157751173375,
    1597359355357393799137,
    1739591759757757151917,
    1931377935975973733737,
]
                     
neg_perfect_cubes = [0 - i for i in pos_perfect_cubes]
perfect_cubes = neg_perfect_cubes[::-1] + pos_perfect_cubes

def odd_dig_cubic(a, b):
    return list(filter(lambda x: a <= x <= b, perfect_cubes))

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