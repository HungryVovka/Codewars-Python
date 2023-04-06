# -----------------------------------------------------------
# You've been given a list that states the daily revenue for each day of the week. Unfortunately, the list has been corrupted and contains extraneous 
# characters. Rather than fix the source of the problem, your boss has asked you to create a program that removes any unneccessary characters and 
# return the corrected list.
# 
# The expected characters are digits, ' $ ', and ' . ' All items in the returned list are expected to be strings.
# 
# For example:
# 
# a1 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']
# remove_char(a1) 
# >>> ['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']
# -----------------------------------------------------------

def remove_char(array):
    answer = []
    for i in array:
        i = "".join(j for j in i if j.isnumeric())
        answer.append("$%s.%s" % (i[:-2], i[-2:]))
    return answer

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