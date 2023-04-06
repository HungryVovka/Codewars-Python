# -----------------------------------------------------------
# Fix the bug in Filtering method
# The method is supposed to remove even numbers from the list and return a list that contains the odd numbers.
# 
# However, there is a bug in the method that needs to be resolved.
# -----------------------------------------------------------

def kata_13_december(lst):
    fix = list()
    for i in range(len(lst)): 
        if lst[i] % 2 != 0: 
            fix.append(lst[i])
    return fix

# or

def kata_13_december(lst):
    return [i for i in lst if i % 2]

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