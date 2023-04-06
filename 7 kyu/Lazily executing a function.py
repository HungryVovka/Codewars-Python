# -----------------------------------------------------------
# Deferring a function execution can sometimes save a lot of execution time in our programs by postponing the execution to the latest possible instant 
# of time, when we're sure that the time spent while executing it is worth it.
# 
# Write a method make_lazy that takes in a function (symbol for Ruby) and the arguments to the function and returns another function (lambda for 
# Ruby) which when invoked, returns the result of the original function invoked with the supplied arguments.
# 
# For example:
# 
# Given a function add
# 
# function add (a, b) {
#   return a + b;
# }
# 
# One could make it lazy as:
# 
# var lazy_value = make_lazy(add, 2, 3);
# 
# The expression does not get evaluated at the moment, but only when you invoke lazy_value as:
# 
# lazy_value() => 5
# 
# The above invokation then performs the sum.
# 
# Please note: The functions that are passed to make_lazy may take one or more arguments and the number of arguments is not fixed.
# -----------------------------------------------------------

def make_lazy(*args):
    f = args[0]
    values = args[1:]
    def lazily_executing():
        return f(*values)
    return lazily_executing

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