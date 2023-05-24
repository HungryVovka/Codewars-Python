# -----------------------------------------------------------
# Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.
# 
# a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.
# 
# The four operators are "add", "subtract", "divide", "multiply".
# 
# A few examples:(Input1, Input2, Input3 --> Output)
# 
# 5, 2, "add"      --> 7
# 5, 2, "subtract" --> 3
# 5, 2, "multiply" --> 10
# 5, 2, "divide"   --> 2.5
# 
# Try to do it without using if statements!
# -----------------------------------------------------------

def arithmetic(a, b, operator):
    arithmetic_dict = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b,
    }
    return arithmetic_dict[operator]

# or

def arithmetic(a, b, operator):
    match operator:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            return a / b

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