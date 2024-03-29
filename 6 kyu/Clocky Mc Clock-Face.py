# -----------------------------------------------------------
# Story
# Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.
# 
# And because the local council has lost most of our tax money to a Nigerian email scam there are no funds to fix the clock properly.
# 
# Instead, they are asking for volunteer programmers to write some code that tell the time by only looking at the remaining hour-hand!
# 
# What a bunch of cheapskates!
# 
# Can you do it?
# 
# Kata
# Given the angle (in degrees) of the hour-hand, return the time in 12 hour HH:MM format. Round down to the nearest minute.
# 
# Examples
# 12:00 = 0 degrees
# 
# 03:00 = 90 degrees
# 
# 06:00 = 180 degrees
# 
# 09:00 = 270 degrees
# 
# 12:00 = 360 degrees
# 
# Notes
# 0 <= angle <= 360
# 
# Do not make any AM or PM assumptions for the HH:MM result. They are indistinguishable for this Kata.
# 
# 3 o'clock is 03:00, not 15:00
# 7 minutes past midnight is 12:07
# 7 minutes past noon is also 12:07
# -----------------------------------------------------------

import math

def what_time_is_it(angle):
    hour = math.floor(angle * 2 / 60)
    minute = math.floor(angle * 2 % 60)
    if hour == 0:
        hour = "12"
    elif hour < 10:
        hour = "0" + str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    return f"{hour}:{minute}"

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