# -----------------------------------------------------------
# Let's build a calculator that can calculate the average for an arbitrary number of arguments.
# 
# The test expects you to provide a Calculator object with an average method:
# 
# Calculator.average()
# 
# The test also expects that when you pass no arguments, it returns 0. The arguments are expected to be integers.
# 
# It expects Calculator.average(3,4,5) to return 4.
# -----------------------------------------------------------

class Calculator:
    @staticmethod
    def average(*args):
        return 0 if not args else sum(args) / len(args)

# or

import statistics

class Calculator:
    @staticmethod
    def average(*args):
        return len(args) and statistics.mean(args)

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