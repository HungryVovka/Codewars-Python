# -----------------------------------------------------------
# Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.
# 
# For example: ["3:1", "2:2", "0:1", ...]
# 
# Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:
# 
# if x > y: 3 points
# if x < y: 0 point
# if x = y: 1 point
# 
# Notes:
# 
# there are 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4
# -----------------------------------------------------------

def points(games):
    score = 0
    for g in games:
        if g[0] > g[2]:
            score += 3
        if g[0] < g[2]:
            continue
        if g[0] == g[2]:
            score += 1
    return score

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