# -----------------------------------------------------------
# What is the answer to life the universe and everything
# 
# Create a function that will make anything true
# 
#     anything({}) != [],          'True'
#     anything('Hello') < 'World', 'True'
#     anything(80) > 81,           'True'
#     anything(re) >= re,          'True'
#     anything(re) <= math,        'True'
#     anything(5) == ord,          'True'
# 
# Source: CheckIO (https://py.checkio.org/ru/mission/solution-for-anything/)
# -----------------------------------------------------------

class anything:
    def __init__(self, any):
        pass
    
    def __eq__(self, any):
        return True
    
    def __ge__(self, any):
        return True
    
    def __gt__(self, any):
        return True 
    
    def __le__(self, any):
        return True
    
    def __lt__(self, any):
        return True
    
    def __ne__(self, any):
        return True

# or

class anything:
    def __init__(self, any):
        pass
    
    def __eq__(self, any):
        return True
    
    __ge__ = __gt__ = __le__ = __lt__ = __ne__ = __eq__

# or

class anything(str):
    __eq__ = __ge__ = __gt__ = __le__ = __lt__ = __ne__ = str

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