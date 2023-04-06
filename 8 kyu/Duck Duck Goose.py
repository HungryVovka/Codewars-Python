# -----------------------------------------------------------
# The objective of Duck, duck, goose is to walk in a circle, tapping on each player's head until one is chosen.
# 
# Task: Given an array of Player objects (an array of associative arrays in PHP) and an index (1-based), return the name of the chosen Player(name is a 
# property of Player objects, e.g Player.name)
# 
# Example:
# 
# duck_duck_goose([a, b, c, d], 1) should return a.name
# duck_duck_goose([a, b, c, d], 5) should return a.name
# duck_duck_goose([a, b, c, d], 4) should return d.name
# 
# // PHP only
# duck_duck_goose([$a, $b, $c, $d], 1); // => $a["name"]
# duck_duck_goose([$a, $b, $c, $d], 5); // => $a["name"]
# duck_duck_goose([$a, $b, $c, $d], 4); // => $d["name"]
# -----------------------------------------------------------

def duck_duck_goose(players, goose):
    ddg = players[(goose % len(players)) - 1]
    return ddg.name

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