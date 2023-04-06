# -----------------------------------------------------------
# Fix the Bugs (Syntax) - My First Kata
# 
# Overview
# Hello, this is my first Kata so forgive me if it is of poor quality.
# 
# In this Kata you should fix/create a program that returns the following values:
# 
# false/False if either a or b (or both) are not numbers
# a % b plus b % a if both arguments are numbers
# 
# You may assume the following:
# 
# If a and b are both numbers, neither of a or b will be 0.
# 
# Language-Specific Instructions
# Javascript and PHP
# 
# In this Kata you should try to fix all the syntax errors found in the code.
# 
# Once you think all the bugs are fixed run the code to see if it works. A correct solution should return the values specified in the overview.
# 
# Extension: Once you have fixed all the syntax errors present in the code (basic requirement), you may attempt to optimise the code or try a different 
# approach by coding it from scratch.
# -----------------------------------------------------------

def my_first_kata(a, b):
    if type(a) != int or type(b) != int:
        return False
    else:
        return a % b + b % a

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