# -----------------------------------------------------------
# Enough is enough!
# Alice and Bob were on a holiday. Both of them took many pictures of the places 
# they've been, and now they want to show Charlie their entire collection. 
# However, Charlie doesn't like these sessions, since the motif usually repeats. He 
# isn't fond of seeing the Eiffel tower 40 times.
# He tells them that he will only sit for the session if they show the same motif at 
# most N times. Luckily, Alice and Bob are able to encode the motif as a number. 
# Can you help them to remove numbers such that their list contains each number 
# only up to N times, without changing the order?
# 
# Task
# Given a list and a number, create a new list that contains each number of list 
# at most N times, without reordering.
# For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3],
# you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 
# being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
# With list [20,37,20,21] and number 1, the result would be [20,37,21].
# -----------------------------------------------------------

def delete_nth(order, max_e):
    occurrences_counter: dict[int, int] = {}
    filtered: list[int] = []
    for n in order:
        count = occurrences_counter.get(n, 0)
        if count < max_e:
            filtered.append(n)
            occurrences_counter[n] = count + 1
        else:
            pass
    return filtered

# -----------------------------------------------------------
# License
# Tasks are the property of Codewars (https://www.codewars.com/) 
# and users of this resource.
# 
# All solution code in this repository 
# is the personal property of Vladimir Rukavishnikov
# (vladimirrukavishnikovmail@gmail.com).
# 
# Copyright (C) 2025 Vladimir Rukavishnikov
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