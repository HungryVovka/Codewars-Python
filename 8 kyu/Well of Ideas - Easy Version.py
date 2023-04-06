# -----------------------------------------------------------
# For every good kata idea there seem to be quite a few bad ones!
# 
# In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if 
# there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.
# -----------------------------------------------------------

def well(x):
    ideas = x.count('good')
    if ideas > 2:
        return 'I smell a series!'
    elif ideas >= 1:
        return 'Publish!'
    else:
        return 'Fail!'

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