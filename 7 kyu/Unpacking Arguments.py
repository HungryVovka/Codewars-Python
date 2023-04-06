# -----------------------------------------------------------
# You must create a function, spread, that takes a function and a list of arguments to be applied to that function. You must make this function return 
# the result of calling the given function/lambda with the given arguments.
# 
# eg:
# 
# spread(someFunction, [1, true, "Foo", "bar"] ) 
# # is the same as...
# someFunction(1, true, "Foo", "bar")
# -----------------------------------------------------------

def spread(func, args):
    return func(*args)

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