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