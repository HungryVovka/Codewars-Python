# -----------------------------------------------------------
# Challenge: Given two null-terminated strings in the arguments "string" and "prefix", determine if "string" starts with the "prefix" string. Return true 
# or false.
# 
# Example:
# 
# startsWith("hello world!", "hello"); // should return true
# startsWith("hello world!", "HELLO"); // should return false
# startsWith("nowai", "nowaisir"); // should return false
# 
# Addendum: For this problem, an empty "prefix" string should always return true for any value of "string".
# 
# If the length of the "prefix" string is greater than the length of the "string", return false.
# 
# The check should be case-sensitive, i.e. startsWith("hello", "HE") should return false, whereas startsWith("hello", "he") should return true.
# 
# The length of the "string" as well as the "prefix" can be defined by the formula: 0 <= length < +Infinity
# 
# No characters should be ignored and/or omitted during the test, e.g. whitespace characters should not be ignored.
# -----------------------------------------------------------

def starts_with(st, prefix):
    return st.startswith(prefix)

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