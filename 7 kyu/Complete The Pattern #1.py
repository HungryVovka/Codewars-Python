# -----------------------------------------------------------
# Task:
# You have to write a function pattern which returns the following Pattern(See Pattern & Examples) upto n number of rows.
# 
# Note:Returning the pattern is not the same as Printing the pattern.
# Rules/Note:
# If n < 1 then it should return "" i.e. empty string.
# There are no whitespaces in the pattern.
# 
# Pattern:
# 1
# 22
# 333
# ....
# .....
# nnnnnn
# 
# Examples:
# 
# pattern(5):
# 
# 1
# 22
# 333
# 4444
# 55555
# 
# pattern(11):
# 
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
# 10101010101010101010
# 1111111111111111111111
# 
# Hint: Use \n in string to jump to next line
# -----------------------------------------------------------

def pattern(n):
    patt = []
    for i in range (1, n + 1):
        patt.append(str(i) * i)
    return "\n".join(patt)

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