# -----------------------------------------------------------
# In this kata, we will make a function to test whether a period is late.
# 
# Our function will take three parameters:
# 
# last - The Date object with the date of the last period
# 
# today - The Date object with the date of the check
# 
# cycleLength - Integer representing the length of the cycle in days
# 
# Return true if the number of days passed from last to today is greater than cycleLength. Otherwise, return false.
# -----------------------------------------------------------

from datetime import date

def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length

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