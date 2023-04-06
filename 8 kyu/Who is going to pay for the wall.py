# -----------------------------------------------------------
# Don Drumphet lives in a nice neighborhood, but one of his neighbors has started to let his house go. Don Drumphet wants to build a wall between 
# his house and his neighbor’s, and is trying to get the neighborhood association to pay for it. He begins to solicit his neighbors to petition to get the 
# association to build the wall. Unfortunately for Don Drumphet, he cannot read very well, has a very limited attention span, and can only remember 
# two letters from each of his neighbors’ names. As he collects signatures, he insists that his neighbors keep truncating their names until two letters 
# remain, and he can finally read them.
# 
# Your code will show Full name of the neighbor and the truncated version of the name as an array. If the number of the characters in name is less than 
# or equal to two, it will return an array containing only the name as is"
# -----------------------------------------------------------

def who_is_paying(name):
    if len(name) > 3:
        return [name, name[:2]]
    return [name]

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