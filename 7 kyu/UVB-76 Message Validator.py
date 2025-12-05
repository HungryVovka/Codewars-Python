# -----------------------------------------------------------
# In Russia, there is an army-purposed station 
# named UVB-76 or "Buzzer". (https://en.wikipedia.org/wiki/UVB-76)
# 
# Most of time specific "buzz" noise is being broadcasted, but on 
# very rare occasions, the buzzer signal is interrupted and a voice 
# transmission in Russian takes place.
# 
# Transmitted messages have always the same format like this:
# 
# MDZHB 01 213 SKIF 38 87 23 95
# 
# or
# 
# MDZHB 80 516 GANOMATIT 21 23 86 25
# 
# Message format consists of following parts:
# 
# Initial keyword "MDZHB";
# Two groups of digits, 2 digits in first and 3 in second ones;
# Some keyword of arbitrary length consisting only of uppercase letters;
# Final 4 groups of digits with 2 digits in each group.
#
# Your task is to write a function that can validate the correct UVB-76 message. 
# Function should return true if message is in correct format and false otherwise.
# -----------------------------------------------------------

import re   # fullmatch

def validate(message: str) -> bool:
    pattern = r"^MDZHB \d{2} \d{3} [A-Z]+(?: \d{2}){4}$"
    return bool(re.fullmatch(pattern, message))

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