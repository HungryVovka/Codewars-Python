# -----------------------------------------------------------
# If/else syntax debug
# While making a game, your partner, Greg, decided to create a function to check if the user is still alive called 
# checkAlive/CheckAlive/check_alive. Unfortunately, Greg made some errors while creating the function.
# 
# checkAlive/CheckAlive/check_alive should return true if the player's health is greater than 0 or false if it is 0 or below.
# 
# The function receives one parameter health which will always be a whole number between -10 and 10.
# -----------------------------------------------------------


def check_alive(health):
    if health <= 0:
        return False
    else:
        return True

# or

def check_alive(health):
    return health > 0

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