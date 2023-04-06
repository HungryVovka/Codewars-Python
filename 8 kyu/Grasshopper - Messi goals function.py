# -----------------------------------------------------------
# Messi goals function
# Messi is a soccer player with goals in three leagues:
# 
# LaLiga
# Copa del Rey
# Champions
# Complete the function to return his total number of goals in all three leagues.
# 
# Note: the input will always be valid.
# 
# For example:
# 
# 5, 10, 2  -->  17
# -----------------------------------------------------------

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# or

def goals(*goals):
    return sum(goals)

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