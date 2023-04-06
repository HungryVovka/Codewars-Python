# -----------------------------------------------------------
# If I were to ask you the size of "hello", what would you say?
# 
# Wait, let me rephrase the question:
# 
# If I were to ask you the total byte size of "hello", how many bytes do you think it takes up?
# 
# I'll give you a hint: it's not 5.
# 
# len("hello")  -->  5
# 
# byte size -->  54
# 
# 54? What?!
# 
# Here's why: every string has to have an encoding (e.g ASCII),the info that makes it an object, as well as all of it's other properites... it would have to 
# take up a bit more than 5 bytes, wouldn't it?
# 
# This might be useful for sending something over a network, where you need to represent the memory size the item takes up.
# 
# Task:
# In this kata, you need to return the number of bytes (aka. memory size) a given object takes up.
# 
# Different variable types will be given, but they will all be valid. Also, random generation for strings takes out of Unicode, not the regular 255 ascii 
# letters.
# 
# p.s: Don't be afraid to use the internet. It "byte" come in handy :)
# 
# Other Examples:
# 
# Object    Bytes    Why?
# ----      ----     ---- 
# "龘"       76      Other character sets take up more room.
# 123        28      Numbers don't have as much info in them. 
# [1,2]      72      Lists have more info stored (e.g index).
# (1,2)      56      Tuples are (kind of) just bowls of data.
# -----------------------------------------------------------

import sys

def total_bytes(byte_me):
    return sys.getsizeof(byte_me)

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