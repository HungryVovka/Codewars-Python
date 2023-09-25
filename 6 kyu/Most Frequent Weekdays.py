# -----------------------------------------------------------
# What is your favourite day of the week? Check if it's the most frequent day of the week in the year.
# 
# You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has to be a list of days 
# sorted by the order of days in week (e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). Week starts with Monday.
# 
# Input: Year as an int.
# 
# Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).
# 
# Preconditions:
# 
# Week starts on Monday.
# Year is between 1583 and 4000.
# Calendar is Gregorian.
# 
# Examples (input -> output):
# * 2427 -> ['Friday']
# * 2185 -> ['Saturday']
# * 2860 -> ['Thursday', 'Friday']
# -----------------------------------------------------------

import datetime

def most_frequent_days(year):
    answer = []
    days_of_week = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
    weekdays_count = [0] * 7
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                d = datetime.date(year, month, day)
                weekday = d.weekday()
                weekdays_count[weekday] += 1
            except:
                break
    most_frequent = max(weekdays_count)
    for i in range(7):
        if weekdays_count[i] == most_frequent:
            answer.append(days_of_week[i])
    return answer

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