# -----------------------------------------------------------
# Frank just bought a new calculator. But, this is no normal calculator. This is a 'Sticky Calculator.
# 
# Whenever you add add, subtract, multiply or divide two numbers the two numbers first stick together:
# 
# For instance:
# 
# 50 + 12 becomes 5012
# and then the operation is carried out as usual:
# 
# (5012) + 12 = 5024
# 
# Task
# It is your job to create a function which takes 3 parameters:
# 
# stickyCalc(operation, val1, val2)
# which works just like Frank's sticky calculator
# 
# Some Examples
# stickyCalc('+', 50, 12)     // Output: (5012 + 12) = 5024
# stickyCalc('-', 7, 5)       // Output: (75 - 5) = 70
# stickyCalc('*', 13, 20)     // Output: (1320 * 20 ) = 26400
# stickyCalc('/', 10, 10)     // Output: (1010 / 10) = 101
# 
# Note
# The calculator only works for positive integers only.
# The calculator rounds any non-integer before operating.
# The calculator rounds any output to nearest integer.
# 
# For example:
# 
# stickyCalc('/', 12.1, 6.8), 18);   
# 12.1 and 6.8 are rounded to 12 and 7 respectively & they 'stick together' to make 127.
# 
# Although 127 / 7 = 18.1428 ; 18 is outputted instead.
# -----------------------------------------------------------

def sticky_calc(operation, val1, val2):
    v1 = round(val1)
    v2 = round(val2)
    val3 = int(str(v1) + str(v2))
    if operation == '+':
        val3 += val2
    if operation == '-':
        val3 -= val2
    if operation == '*':
        val3 *= round(val2)
    if operation == '/':
        val3 /= round(val2)
    return (round(val3))

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