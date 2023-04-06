# -----------------------------------------------------------
# #~For Kids Challenges~#
# Your task is easy, write a function that takes an date in format d/m/Y(String) and return what day of the week it was(String).
# Example: "21/01/2017" -> "Saturday", "31/03/2017" -> "Friday"
# Have fun!
# -----------------------------------------------------------

import datetime

def day_of_week(date):
    day, month, year = (int(x) for x in date.split('/'))
    answer = datetime.date(year, month, day)
    return answer.strftime("%A")

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