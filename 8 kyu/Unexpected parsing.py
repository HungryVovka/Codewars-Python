# -----------------------------------------------------------
# Here is a piece of code:
# 
# def get_status(is_busy):
#     status = "busy" if is_busy else "available"
#     return status
# 
# Expected Behaviour
# Function should return a dictionary/Object/Hash with "status" as a key, whose value can : "busy" or "available" depending on the truth value 
# of the argument is_busy.
# 
# But as you will see after clicking RUN or ATTEMPT this code has several bugs, please fix them.
# -----------------------------------------------------------

def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return {"status" : status}

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