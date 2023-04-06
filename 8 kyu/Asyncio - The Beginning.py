# -----------------------------------------------------------
# Story
# As you walk the streets with your crush beside you, you are thinking about the world and how everything works... Wait!! Your crush? Shit, you are 
# dreaming again.
# 
# Task
# Now implement a coroutine dreaming which sleeps for n seconds and then returns m ** n without entirely blocking the execution of other 
# coroutines that might be running.
# 
# Note
# 0 < n < 7
# 
# 0 < m < 100
# -----------------------------------------------------------

from asyncio import sleep

def dreaming(n, m):
    return sleep(n, m**n) 

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