# -----------------------------------------------------------
# Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.
# 
# For example n = 3 result in:
# 
# "I\n I\n  I"
# or printed:
# 
# I
#  I
#   I
# Another example, a 7-step stairs should be drawn like this:
# 
# I
#  I
#   I
#    I
#     I
#      I
#       I
# -----------------------------------------------------------

def draw_stairs(n):
    answer = ''
    for s in range (0, n-1):
        answer += ' ' * s + 'I\n'
    answer += ' ' * (n-1) + 'I'
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