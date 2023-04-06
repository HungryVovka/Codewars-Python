# -----------------------------------------------------------
# In this kata we are focusing on the Numpy python package. You must write a function called looper which takes three integers 
# start, stop and number as input and returns a list from start to stop with number total values in the list. Five examples are shown below:
# 
# looper(1, 5, 1) = [1.0]
# looper(1, 5, 2) = [1.0, 5.0]
# looper(1, 5, 3) = [1.0, 3.0, 5.0]
# looper(1, 5, 4) = [1.0, 2.333333333333333, 3.6666666666666665, 5.0]
# looper(1, 5, 5) = [1.0, 2.0, 3.0, 4.0, 5.0]
# -----------------------------------------------------------

import numpy as np

def looper(start, stop, number):
    return list(np.linspace(start, stop, number))

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