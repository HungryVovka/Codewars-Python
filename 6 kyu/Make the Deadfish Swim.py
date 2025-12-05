# -----------------------------------------------------------
# Create a parser to interpret and execute the Deadfish language.
# 
# Deadfish operates on a single value in memory, which is initially set to 0.
# 
# It uses four single-character commands:
# 
# i: Increment the value
# d: Decrement the value
# s: Square the value
# o: Output the value to a result array
# 
# All other instructions are no-ops and have no effect.
# 
# Examples
# Program "iiisdoso" should return numbers [8, 64].
# Program "iiisdosodddddiso" should return numbers [8, 64, 3600].
# -----------------------------------------------------------

def parse(data: str) -> list[int]:
    current_value = 0
    output_values: list[int] = []
    for command in data:
        match command:
            case 'i':
                current_value += 1
            case 'd':
                current_value -= 1
            case 's':
                current_value *= current_value
            case 'o':
                output_values.append(current_value)
            case _:
                pass
    return output_values

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