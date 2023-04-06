# -----------------------------------------------------------
# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
# 
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
# 
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# 
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# 
# The test cases contain numbers only by mistake.
# -----------------------------------------------------------

def correct(s):
    s = s.replace("5", "S")
    s = s.replace("0", "O")
    s = s.replace("1", "I")
    return s

# or

def correct(s):
    correct = s.maketrans("501", "SOI")
    return s.translate(correct)

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