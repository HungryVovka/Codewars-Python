# -----------------------------------------------------------
# Create a function called _if which takes 3 arguments: a boolean value bool and 2 functions (which do not take any parameters): func1 and
# func2
# 
# When bool is truth-ish, func1 should be called, otherwise call the func2.
# 
# Example:
# def truthy(): 
#   print("True")
#  
# def falsey(): 
#   print("False")
#   
# _if(True, truthy, falsey)
# prints 'True' to the console
# -----------------------------------------------------------

def _if(bool, func1, func2):
    if bool == True:
        return func1()
    else:
        return func2()

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