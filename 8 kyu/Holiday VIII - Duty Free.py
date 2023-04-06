# -----------------------------------------------------------
# The purpose of this kata is to work out just how many bottles of duty free whiskey you would have to buy such that the saving over the normal high 
# street price would effectively cover the cost of your holiday.
# 
# You will be given the high street price (normPrice), the duty free discount (discount) and the cost of the holiday.
# 
# For example, if a bottle cost £10 normally and the discount in duty free was 10%, you would save £1 per bottle. If your holiday cost £500, the answer 
# you should return would be 500.
# 
# All inputs will be integers. Please return an integer. Round down.
# -----------------------------------------------------------

import math

def duty_free(price, discount, holiday_cost):
    return math.floor(holiday_cost / price / discount * 100)

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