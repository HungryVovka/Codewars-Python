# -----------------------------------------------------------
# Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.
# 
# You need to consider the following ratings:
# 
# Terrible: tip 0%
# Poor: tip 5%
# Good: tip 10%
# Great: tip 15%
# Excellent: tip 20%
# 
# The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:
# 
# "Rating not recognised" in Javascript, Python and Ruby...
# ...or null in Java
# ...or -1 in C#
# 
# Because you're a nice person, you always round up the tip, regardless of the service.
# -----------------------------------------------------------

import math

def calculate_tip(amount, rating):
    try:
        tips = {
            "terrible" : 0,
            "poor" : 0.05,
            "good" : 0.1,
            "great" : 0.15,
            "excellent" : 0.2,
        }
        rating = rating.lower()
        return math.ceil(amount * tips.get(rating))
    except:
        return "Rating not recognised"

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