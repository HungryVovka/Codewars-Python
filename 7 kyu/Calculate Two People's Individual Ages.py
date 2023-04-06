# -----------------------------------------------------------
# Create a function that takes in the sum and age difference of two people, calculates their individual ages, and returns a pair of values (oldest age 
# first) if those exist or null/None if:
# 
# sum < 0
# difference < 0
# 
# Either of the calculated ages come out to be negative
# -----------------------------------------------------------

def get_ages(sum_, difference):
    if sum_ < 0 or difference < 0:
        return(None)
    if sum_ >= 0 and difference >= 0:
        second = (sum_ - difference) / 2
        first = second + difference
        if first >= 0 and second >= 0:
            return(first, second)
        else:
            return(None)

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