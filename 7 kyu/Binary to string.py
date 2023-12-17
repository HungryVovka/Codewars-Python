# -----------------------------------------------------------
# Your computer has forgotten how to speak ASCII! (or Unicode, whatever) It can only communicate in binary, and it has something important to tell 
# you. Write a function which will receive a long string of binary code and convert it to a string. Remember, in Python binary output starts with '0b'.
# 
# As an example: binary_to_string('0b10000110b11000010b1110100') == 'Cat'
# 
# Input may consist of upper and lower case letters and numbers, in binary form of course, as well as special symbols. The input to your function will 
# always be one string of binary.
# -----------------------------------------------------------

def binary_to_string(binary):
    answer = ""
    binary_letters = binary.split("0b")
    for i in binary_letters:
        if i != "":
            answer += chr(int(i, 2))
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