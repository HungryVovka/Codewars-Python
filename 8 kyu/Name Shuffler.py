# -----------------------------------------------------------
# Write a function that returns a string in which firstname is swapped with last name.
# 
# Example(Input --> Output)
# 
# "john McClane" --> "McClane john"
# -----------------------------------------------------------

def name_shuffler(str_):
    arr = str_.split()
    return(arr[1] + " " + arr[0])

# or

def name_shuffler(str_):
    return " ".join(reversed(str_.split()))

# or

def name_shuffler(str_):
    return " ".join(str_.split()[::-1])

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