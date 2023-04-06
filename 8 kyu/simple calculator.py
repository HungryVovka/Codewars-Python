# -----------------------------------------------------------
# You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.
# 
# Your function will accept three arguments:
# The first and second argument should be numbers.
# The third argument should represent a sign indicating the operation to perform on these two numbers.
# 
# if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.
# 
# Example:
# calculator(1, 2, '+') => 3
# calculator(1, 2, '$') # result will be "unknown value"
# 
# Good luck!
# -----------------------------------------------------------

def calculator(x, y, op):
    if op == "+" and type(x) == type(y) == int:
        return x + y
    if op == "-" and type(x) == type(y) == int:
        return x - y
    if op == "*" and type(x) == type(y) == int:
        return x * y
    if op == "/" and type(x) == type(y) == int and y != 0:
        return x / y
    else:
        return "unknown value"

# or

def calculator(x,y,op):
    try:
        assert op in "+-*/"
        assert type(x) == int
        assert type(y) == int
        return eval("%d%s%d" % (x, op, y))
    except:
        return "unknown value"

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