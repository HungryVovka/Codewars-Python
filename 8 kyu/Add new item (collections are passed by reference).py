# -----------------------------------------------------------
# Add an item to the list:
# 
# AddExtra method adds a new item to the list and returns the list. The new item can be any object, and it does not matter. (lets say you add an integer 
# value, like 13)
# 
# In our test case we check to assure that the returned list has one more item than the input list. However the method needs some modification to 
# pass this test.
# 
# P.S. You have to create a new list and add a new item to that. (This Kata is originally designed for C# language and it shows that adding a new item to 
# the input list is not going to work, even though the parameter is passed by value, but the value is poining to the reference of list and any change on 
# parameter will be seen by caller)
# -----------------------------------------------------------

def add_extra(list_of_numbers):
    return list_of_numbers + ["HungryVovka"]

# or

def add_extra(list_of_numbers):
    return list_of_numbers + [42]

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