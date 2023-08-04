# -----------------------------------------------------------
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the 
# Caesar cipher.
# 
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, 
# they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
# 
# Please note that using encode is considered cheating.
# -----------------------------------------------------------

def caesar_cipher(i, a):
    return chr((ord(i) - ord(a) + 13) % 26 + ord(a))

def rot13(message):
    answer = ""
    for i in message:
        if i.isalpha():
            if i.isupper():
                answer += caesar_cipher(i, "A")
            else:
                answer += caesar_cipher(i, "a")
        else:
            answer += i
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