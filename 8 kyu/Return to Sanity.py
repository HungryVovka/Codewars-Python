# -----------------------------------------------------------
# This function should return an object, but it's not doing what's intended. What's wrong?
# -----------------------------------------------------------

def mystery():
    results = {
        'sanity': 'Hello',
    }
    return results

# or

def mystery():
    results = {
        'sanity': 'Hello',
    }
    return \
    results

# or

def mystery(return_to_sanity = {"sanity" : "Hello"}):
    return return_to_sanity

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