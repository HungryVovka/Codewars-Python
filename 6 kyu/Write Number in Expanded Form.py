# -----------------------------------------------------------
# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
# 
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# 
# NOTE: All numbers will be whole numbers greater than 0.
# -----------------------------------------------------------

def expanded_form(num):
    listed_num = list(str(num))
    answer = []
    for i, j in enumerate(listed_num):
        if j != "0":
            answer.append(j + "0" * (len(listed_num) - i - 1))
    return " + ".join(answer)

# or

def expanded_form(num):
    num_str = str(num)
    answer = []
    i = (len(num_str) - 1)
    for j in num_str:
        if j != "0":
            answer.append(j + "0" * i)
        i -= 1
    return " + ".join(answer)

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