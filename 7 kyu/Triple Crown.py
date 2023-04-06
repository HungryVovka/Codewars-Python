# -----------------------------------------------------------
# Welcome to the world of the National Football League!
# 
# In the NFL the Triple Crown is given when a receiver has the most receiving yards, the most receiving touchdowns and the most receptions in a 
# single season.
# 
# This year Cooper Kupp managed to get it, however it is quite rare because the last one was in 2005 by Steve Smith.
# 
# Now you will receive a dictionary with the following keys (will always contain each):
# 
# Cooper Kupp
# 
# Justin Jefferson
# 
# Davante Adams
# 
# Each key will have another dictionary as their values with the following keys:
# 
# Receiving yards (value between 1500-2000)
# 
# Receiving touchdowns (value between 10-20)
# 
# Receptions (value between 90-120)
# 
# If one receiver has the most in each category you have to return his name. If there is no receiver with the most values in all categories you should 
# return 'None of them'.
# 
# Example:
# 
# {
#   'Cooper Kupp': 
#     {
#     'Receiving yards': 1786, 
#     'Receiving touchdowns': 18, 
#     'Receptions': 117
#     },
#   'Justin Jefferson': 
#     {
#     'Receiving yards': 1700, 
#     'Receiving touchdowns': 17, 
#     'Receptions': 115
#     },
#   'Davante Adams': 
#     {
#     'Receiving yards': 1650, 
#     'Receiving touchdowns': 16, 
#     'Receptions': 110
#     }
# }
# 
# # The output should be 'Cooper Kupp' since he has more receiving yards, more receiving touchdowns and more receptions as well
# Example with two receivers sharing values in at least one category:
# 
# {
#   'Cooper Kupp': 
#     {
#     'Receiving yards': 1900, 
#     'Receiving touchdowns': 18, 
#     'Receptions': 117
#     },
#   'Justin Jefferson': 
#     {
#     'Receiving yards': 1800, 
#     'Receiving touchdowns': 17, 
#     'Receptions': 116
#     },
#   'Davante Adams': 
#     {
#     'Receiving yards': 1900, 
#     'Receiving touchdowns': 18, 
#     'Receptions': 110
#     }
# }
# 
# # The output should be 'None of them' since they are tied on receiving yards and receiving touchdowns
# -----------------------------------------------------------

def triple_crown(receivers):
    for i in receivers:
        if all(receivers[i][b] > receivers[a][b] \
               for b in receivers[i] for a in receivers \
               if i != a):
            return i
    return "None of them"

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