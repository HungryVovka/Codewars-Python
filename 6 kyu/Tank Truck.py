# -----------------------------------------------------------
# To introduce the problem think to my neighbor who drives a tanker truck. The level indicator is down and he is worried because he does not know if 
# he will be able to make deliveries. We put the truck on a horizontal ground and measured the height of the liquid in the tank.
# 
# Fortunately the tank is a perfect cylinder and the vertical walls on each end are flat. The height of the remaining liquid is h, the diameter of the 
# cylinder base is d, the total volume is vt (h, d, vt are positive or null integers). You can assume that h <= d.
# 
# Could you calculate the remaining volume of the liquid? Your function tankvol(h, d, vt) returns an integer which is the truncated result (e.g floor) 
# of your float calculation.
# 
# Examples:
# tankvol(40,120,3500) should return 1021 (calculation gives about: 1021.26992027)
# 
# tankvol(60,120,3500) should return 1750
# 
# tankvol(80,120,3500) should return 2478 (calculation gives about: 2478.73007973)
# -----------------------------------------------------------

import math

def tankvol(h, d, vt):
    return math.floor(((4 * vt) / (d**2 * math.pi)) * \
                      ((d / 2)**2 * math.acos(1 - h / (d / 2)) - ((d / 2) - h) * \
                       math.sqrt(h * (d - h))))

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