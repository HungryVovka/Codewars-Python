# -----------------------------------------------------------
# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with 
# letters from a to m.
# 
# The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the 
# printer used three times color a, four times color b, one time color h then one time color a...
# 
# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with 
# letters not from a to m.
# 
# You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose 
# numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.
# 
# The string has a length greater or equal to one and contains only letters from ato z.
# 
# Examples:
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"
# 
# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"
# -----------------------------------------------------------

def printer_error(s):
    error = 0
    good = "abcdefghijklm"
    for i in s:
        if i not in good:
            error += 1
    return f"{error}/{len(s)}"

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