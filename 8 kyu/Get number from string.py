# -----------------------------------------------------------
# Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56
# 
# Function:
# 
# getNumberFromString(s)
# -----------------------------------------------------------

string_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def get_number_from_string(string):
    answer = ""
    string = list(string)
    for i in string:
        if i in string_numbers:
            answer += i
    return int(answer)

# or

def get_number_from_string(string):
    answer = [i for i in string if i.isdigit()]
    return int("".join(answer))

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