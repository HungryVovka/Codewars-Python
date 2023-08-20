# -----------------------------------------------------------
# The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of 
# saying "Eureka"? Because this sum gives the same number: 89 = 8^1 + 9^2
#  
# 
# The next number in having this property is 135:
# 
# See this property again: 135 = 1^1 + 3^2 + 5^3
#  
# 
# Task
# We need a function to collect these numbers, that may receive two integers a, b that defines the range [a,b] (inclusive) and outputs a list of the 
# sorted numbers in the range that fulfills the property described above.
# 
# Examples
# Let's see some cases (input -> output):
# 
# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
# 
# If there are no numbers of this kind in the range [a,b] the function should output an empty list.
# 
# 90, 100 --> []
# 
# Enjoy it!!
# -----------------------------------------------------------

def sum_dig_pow(a, b):
    answer = []
    for i in range(a, b + 1):
        check = [int(k)**(j + 1) for j, k in enumerate(str(i))]
        if i == sum(check):
            answer.append(i)
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