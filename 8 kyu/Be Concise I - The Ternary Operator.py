# -----------------------------------------------------------
# Be Concise I - The Ternary Operator
# You are given a function describeAge / describe_age that takes a parameter age (which will always be a positive integer) and does the following:
# 
# If the age is 12 or lower, it return "You're a(n) kid"
# If the age is anything between 13 and 17 (inclusive), it return "You're a(n) teenager"
# If the age is anything between 18 and 64 (inclusive), it return "You're a(n) adult"
# If the age is 65 or above, it return "You're a(n) elderly"
# 
# Your task is to shorten the code as much as possible. Note that submitting the given code will not work because there is a character limit of 145.
# 
# I'll give you a few hints:
# The title itself is a hint - if you're not sure what to do, always research any terminology in this description that you have not heard of!
# Don't you think the whole "You're a(n) <insert_something_here>" is very repetitive? ;) Perhaps we can shorten it?
# Write everything in one line, \n and other whitespaces counts.
# 
# Whatever you do, do not change what the function does. Good luck :)
# -----------------------------------------------------------

def describe_age(x):return"You're a(n) "+("elderly" if x>64 else ("adult" if x>17 else ("teenager" if x>12 else "kid")))

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