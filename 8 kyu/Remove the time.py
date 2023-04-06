# -----------------------------------------------------------
# You're re-designing a blog and the blog's posts have the following format for showing the date and time a post was made:
# 
# Weekday Month Day, time e.g., Friday May 2, 7pm
# 
# You're running out of screen real estate, and on some pages you want to display a shorter format, Weekday Month Day that omits the time.
# 
# Write a function, shortenToDate, that takes the Website date/time in its original string format, and returns the shortened format.
# 
# Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm". Assume shortenToDate's output will be the shortened string, e.g., 
# "Friday May 2".
# -----------------------------------------------------------

def shorten_to_date(long_date):
    return long_date[:list(long_date).index(",")]

# or

def shorten_to_date(long_date):
    return long_date.split(",")[0]

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