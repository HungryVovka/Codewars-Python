# -----------------------------------------------------------
# Given a list of lists containing only 1s and 0s, return a new list that differs from list 1 in its first element, list 2 in its second element, list 3 in its 3rd 
# element, and so on.
# 
# cantor([[0,0,0],
#         [1,1,1],
#         [0,1,0]]) = [1,0,1]
# 
# cantor([[1,0,0],
#         [0,1,0],
#         [0,0,1]]) = [0,0,0]
#         
# The nested list will always be perfectly square. Your solution should be a list containing only 1s and 0s.
# 
# See Wikipedia for background (if you're interested; it won't help you solve the kata). Obviously this kata is not the same because the lists are not 
# infinite so it doesn't really prove anything -- consider it a tribute...
# -----------------------------------------------------------

def cantor(nested_list):
    answer = []
    for i in range(len(nested_list)):
        answer.append(differs(nested_list[i][i]))
    return answer
    
def differs(x):
    return 0 if x == 1 else 1

# or

def cantor(nested_list):
    answer = []
    for i in range(len(nested_list)):
        answer.append(not(nested_list[i][i]))
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