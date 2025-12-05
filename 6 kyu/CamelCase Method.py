# -----------------------------------------------------------
# Write a method (or function, depending on the language) that converts a string 
# to camelCase, that is, all words must have their first letter capitalized and spaces 
# must be removed.
# 
# Examples (input --> output):
# "hello case" --> "HelloCase"
# "camel case word" --> "CamelCaseWord"
# 
# Don't forget to rate this kata! Thanks :)
# -----------------------------------------------------------

def camel_case(s: str) -> str:
    answer: list[str] = []
    make_upper = True
    for current_char in s:
        if current_char.isspace():
            make_upper = True
            continue
        if make_upper:
            answer.append(current_char.upper())
            make_upper = False
        else:
            answer.append(current_char)
    return "".join(answer)

# -----------------------------------------------------------
# License
# Tasks are the property of Codewars (https://www.codewars.com/) 
# and users of this resource.
# 
# All solution code in this repository 
# is the personal property of Vladimir Rukavishnikov
# (vladimirrukavishnikovmail@gmail.com).
# 
# Copyright (C) 2025 Vladimir Rukavishnikov
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