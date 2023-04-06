# -----------------------------------------------------------
# The aim of this kata is to determine the number of sub-function calls made by an unknown function.
# 
# You have to write a function named count_calls which:
# 
# takes as parameter a function and its arguments (args, kwargs)
# 
# calls the function
# 
# returns a tuple containing:
# 
# the number of function calls made inside it and inside all the sub-called functions recursively
# 
# the function return value.
# 
# NB: The call to the function itself is not counted.
# 
# HINT: The sys module may come in handy.
# -----------------------------------------------------------

from sys import settrace

count = 0

def count_calls(func, *args, **kwargs):
    calls = [-1]
    
    def trace(frame, event, arg):
        """System's trace function."""
        global count
        if event == "call":
            count += 1
            calls[0] += 1
        return trace
    
    settrace(trace)
    rv = func(*args, **kwargs)
    return calls[0], rv

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