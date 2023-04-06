# -----------------------------------------------------------
# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to 
# green again.
# 
# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the 
# light should change to.
# 
# For example, when the input is green, output should be yellow.
# -----------------------------------------------------------

def update_light(current):
    traffic = ['green', 'yellow', 'red']
    if current == 'green':
        return traffic[1]
    if current == 'yellow':
        return traffic[2]
    if current == 'red':
        return traffic[0]

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