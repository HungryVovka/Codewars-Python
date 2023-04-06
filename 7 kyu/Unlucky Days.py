# -----------------------------------------------------------
# Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.
# 
# Find the number of Friday 13th in the given year.
# 
# Input: Year in Gregorian calendar as integer.
# 
# Output: Number of Black Fridays in the year as an integer.
# 
# Examples:
# 
# unluckyDays(2015) == 3
# unluckyDays(1986) == 1
# -----------------------------------------------------------

import datetime

def unlucky_days(year):
    friday13 = 0
    for i in range(12):
        if datetime.date(year, i + 1, 13).weekday() == 4:
            friday13 += 1
    return friday13

# or

import datetime

def unlucky_days(year):
    return sum(datetime.date(year, month, 13).weekday() == 4 for month in range(1, 13))

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