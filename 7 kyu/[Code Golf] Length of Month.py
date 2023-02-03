# -----------------------------------------------------------
# Task
# Return the length of the given month in the given year.
# 
# Your code can be maximum 90 characters long.
# 
# My other katas
# If you enjoyed this kata then please try my other katas! :-)
# 
# Translations are welcome!
# -----------------------------------------------------------

import calendar

last_day = lambda year,month: calendar.monthrange(year,month)[1]