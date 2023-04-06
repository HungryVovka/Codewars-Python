# -----------------------------------------------------------
# Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second 
# parameter, vacation is true whenever you are on vacation.
# 
# The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an 
# 	alarm). It should return false otherwise. Examples:
# 
# setAlarm(true, true) -> false
# setAlarm(false, true) -> false
# setAlarm(false, false) -> false
# setAlarm(true, false) -> true
# -----------------------------------------------------------

def set_alarm(employed, vacation):
    return employed and not vacation

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