# -----------------------------------------------------------
# A variation of determining leap years, assuming only integers are used and years can be negative and positive.
# 
# Write a function which will return the days in the year and the year entered in a string. For example:
# 
# year_days(2000) returns "2000 has 366 days"
# 
# There are a few assumptions we will accept the year 0, even though there is no year 0 in the Gregorian Calendar.
# 
# Also the basic rule for validating a leap year are as follows
# 
# Most years that can be divided evenly by 4 are leap years.
# 
# Exception: Century years are NOT leap years UNLESS they can be evenly divided by 400.
# 
# So the years 0, -64 and 2016 will return 366 days. Whilst 1974, -10 and 666 will return 365 days.
# -----------------------------------------------------------

def year_days(year):
    days_in_year = 365
    if year % 400 == 0 or (year % 4 == 0 and year % 100):
        days_in_year = 366
    return f"{year} has {days_in_year} days"

# or

import calendar

def year_days(year):
    days_in_year = calendar.isleap(year) + 365
    return f"{year} has {days_in_year} days"

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