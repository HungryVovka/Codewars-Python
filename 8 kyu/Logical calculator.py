# -----------------------------------------------------------
# Your Task
# Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially applying the operator to the values in the 
# array.
# 
# Examples
# booleans = [True, True, False], operator = "AND"
# True AND True -> True
# True AND False -> False
# return False
# booleans = [True, True, False], operator = "OR"
# True OR True -> True
# True OR False -> True
# return True
# booleans = [True, True, False], operator = "XOR"
# True XOR True -> False
# False XOR False -> False
# return False
# 
# Input
# an array of Boolean values (1 <= array_length <= 50)
# a string specifying a logical operator: "AND", "OR", "XOR"
# 
# Output
# A Boolean value (True or False).
# -----------------------------------------------------------

def logical_calc(array, op):
    answer = array[0]
    for i in array[1:]:
        if op == "AND":
            answer = answer and i
        elif op == "OR":
            answer = answer or i
        elif op == "XOR":
            answer = answer != i
    return answer

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