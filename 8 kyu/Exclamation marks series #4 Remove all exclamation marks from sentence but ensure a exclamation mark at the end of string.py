# -----------------------------------------------------------
# Description:
# Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input 
# data is always a non empty string, no need to verify it.
# 
# Examples
# remove("Hi!") === "Hi!"
# remove("Hi!!!") === "Hi!"
# remove("!Hi") === "Hi!"
# remove("!Hi!") === "Hi!"
# remove("Hi! Hi!") === "Hi Hi!"
# remove("Hi") === "Hi!"
# -----------------------------------------------------------

def remove(s):
    return s.replace("!", "") + "!"

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