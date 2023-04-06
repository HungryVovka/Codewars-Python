# -----------------------------------------------------------
# Create a function that takes a number as an argument and returns a grade based on that number.
# 
# Score											  Grade
# Anything greater than 1 or less than 0.6		    "F"
# 0.9 or greater									"A"
# 0.8 or greater									"B"
# 0.7 or greater									"C"
# 0.6 or greater									"D"
# 
# Examples:
# 
# grader(0)   should be "F"
# grader(1.1) should be "F"
# grader(0.9) should be "A"
# grader(0.8) should be "B"
# grader(0.7) should be "C"
# grader(0.6) should be "D"
# -----------------------------------------------------------

grade = ["A", "B", "C", "D", "F"]

def grader(score):
    if 1 >= score >= 0.9: return grade[0]
    elif 0.9 > score >= 0.8: return grade[1]
    elif 0.8 > score >= 0.7: return grade[2]
    elif 0.7 > score >= 0.6: return grade[3]
    else: return grade[4]

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