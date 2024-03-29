# -----------------------------------------------------------
# An NBA game runs 48 minutes (Four 12 minute quarters). Players do not typically play the full game, subbing in and out as necessary. Your job is to 
# extrapolate a player's points per game if they played the full 48 minutes.
# 
# Write a function that takes two arguments, ppg (points per game) and mpg (minutes per game) and returns a straight extrapolation of ppg per 48 
# minutes rounded to the nearest tenth. Return 0 if 0.
# 
# Examples:
# 
# nba_extrap(12, 20) # 28.8
# nba_extrap(10, 10) # 48
# nba_extrap(5, 17) # 14.1
# nba_extrap(0, 0) # 0
# 
# Notes:
# All inputs will be either be an integer or float.
# Follow your dreams!
# -----------------------------------------------------------

def nba_extrap(ppg, mpg):
    if ppg == 0 or mpg == 0:
        return 0
    return round((ppg / mpg * 48), 1)

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