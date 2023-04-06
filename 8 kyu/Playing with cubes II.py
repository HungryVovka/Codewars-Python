# -----------------------------------------------------------
# Hey Codewarrior!
# 
# You already implemented a Cube class, but now we need your help again! I'm talking about constructors. We don't have one. Let's code two: One 
# taking an integer and one handling no given arguments!
# 
# Also we got a problem with negative values. Correct the code so negative values will be switched to positive ones!
# 
# The constructor taking no arguments should assign 0 to Cube's Side property.
# -----------------------------------------------------------

class Cube(object):
    def __init__(self, side = 0):
        """Negative values will be switched to positive ones."""
        self._side = abs(side)
    
    def get_side(self):
        """Return the side of the Cube."""
        return self._side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = abs(new_side)

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