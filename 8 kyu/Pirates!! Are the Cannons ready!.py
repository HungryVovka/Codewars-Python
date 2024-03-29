# -----------------------------------------------------------
# Ahoy Matey!
# 
# Welcome to the seven seas.
# 
# You are the captain of a pirate ship.
# 
# You are in battle against the royal navy.
# 
# You have cannons at the ready.... or are they?
# 
# Your task is to check if the gunners are loaded and ready, if they are: Fire!
# 
# If they aren't ready: Shiver me timbers!
# 
# Your gunners for each test case are 2, 3 or 4.
# 
# When you check if they are ready their answers are in a dictionary and will either be: aye or nay
# 
# Firing with less than all gunners ready is non-optimum (this is not fire at will, this is fire by the captain's orders or walk the plank, dirty sea-dog!)
# 
# If all answers are 'aye' then Fire! if one or more are 'nay' then Shiver me timbers!
# 
# Also, check out the new Pirates!! Kata: https://www.codewars.com/kata/57e2d5f473aa6a476b0000fe
# -----------------------------------------------------------

def cannons_ready(gunners):
    ready, not_ready = "Fire!", "Shiver me timbers!"
    if "nay" in gunners.values():
        return not_ready
    return ready

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