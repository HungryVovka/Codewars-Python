# -----------------------------------------------------------
# Complete the function caffeineBuzz, which takes a non-zero integer as its argument.
# 
# If the integer is divisible by 3, return the string "Java".
# 
# If the integer is divisible by 3 and divisible by 4, return the string "Coffee"
# 
# If one of the condition above is true and the integer is even, add "Script" to the end of the string.
# 
# If none of the condition is true, return the string "mocha_missing!"
# 
# caffeineBuzz(1)   => "mocha_missing!"
# caffeineBuzz(3)   => "Java"
# caffeineBuzz(6)   => "JavaScript"
# caffeineBuzz(12)  => "CoffeeScript"
# -----------------------------------------------------------

def caffeine_buzz(n):
    if n % 12 == 0:
        return "CoffeeScript"
    elif n % 6 == 0:
        return "JavaScript"
    elif n % 3 == 0:
        return "Java"
    else:
        return "mocha_missing!"

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