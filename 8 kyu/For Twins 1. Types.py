# -----------------------------------------------------------
# Prolog:
# This kata series was created for friends of mine who just started to learn programming. Wish you all the best and keep your mind open and sharp!
# 
# Task:
# Write a function that will accept two parameters: variable and type and check if type of variable is matching type. Return true if types 
# match or false if not.
# 
# Examples:
# 42, "int"    --> True
# "42", "int"  --> False
# -----------------------------------------------------------

def type_validation(variable, _type):
    return str(variable.__class__.__name__) in _type

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