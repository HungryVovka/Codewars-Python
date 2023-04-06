# -----------------------------------------------------------
# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form 
# of the Roman numeral.
# 
# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and 
# skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman 
# numeral for 1666, "MDCLXVI", uses each letter in descending order.
# 
# Example:
# 
# solution('XXI') # should return 21
# 
# Help:
# 
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
# 
# Courtesy of rosettacode.org
# -----------------------------------------------------------

def solution(r):
    roman = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000,
             'IV': 4,
             'IX': 9,
             'XL': 40,
             'XC': 90,
             'CD': 400,
             'CM': 900}
    i = 0
    num = 0
    while i < len(r):
        if i + 1 < len(r) and r[i:i + 2] in roman:
            num += roman[r[i:i + 2]]
            i += 2
        else:
            num += roman[r[i]]
            i += 1
    return num

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