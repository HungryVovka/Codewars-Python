# -----------------------------------------------------------
# You are the owner of a box making company.
# 
# Your company can produce any equal sided polygon box, but plenty of your customers want to transport circular objects in these boxes. Circles are a 
# very common shape in the consumer industry. Tin cans, glasses, tyres and CD's are a few examples of these.
# 
# As a result you decide to add this information on your boxes: The largest (diameter) circular object that can fit into a given box.
# -----------------------------------------------------------

import math

def circle_diameter(sides, side_length): 
    return side_length * math.cos(math.pi / sides) / math.sin(math.pi / sides)

# or

import math

def circle_diameter(sides, side_length): 
    return side_length / math.tan(math.pi / sides)

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