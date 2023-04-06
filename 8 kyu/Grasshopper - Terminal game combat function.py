# -----------------------------------------------------------
# Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health 
# can't be less than 0.
# -----------------------------------------------------------

def combat(health, damage):
    if health < damage:
        return 0
    return health - damage

# or

def combat(health, damage):
    return 0 if health < damage else health - damage

# or

def combat(health, damage):
    return max(health - damage, 0)

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