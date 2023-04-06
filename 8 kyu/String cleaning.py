# -----------------------------------------------------------
# Your boss decided to save money by purchasing some cut-rate optical character recognition software for scanning in the text of old novels to your 
# database. At first it seems to capture words okay, but you quickly notice that it throws in a lot of numbers at random places in the text.
# 
# Examples (input -> output)
# '! !'                 -> '! !'
# '123456789'           -> ''
# 'This looks5 grea8t!' -> 'This looks great!'
# 
# Your harried co-workers are looking to you for a solution to take this garbled text and remove all of the numbers. Your program will take in a string 
# and clean out all numeric characters, and return a string with spacing and special characters ~#$%^&!@*():;"'.,? all intact.
# -----------------------------------------------------------

def string_clean(s):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for n in numbers:
        s = s.replace(n, '')
    return s

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