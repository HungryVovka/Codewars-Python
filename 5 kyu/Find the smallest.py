# -----------------------------------------------------------
# You have a positive number n consisting of digits. You can do at most one operation: Choosing the index of a digit in the number, remove this digit at 
# that index and insert it back to another or at the same place in the number in order to find the smallest number you can get.
# 
# Task:
# Return an array or a tuple or a string depending on the language (see "Sample Tests") with
# 
# the smallest number you got
# the index i of the digit d you took, i as small as possible
# the index j (as small as possible) where you insert this digit d to have the smallest number.
# 
# Examples:
# smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"
# 
# 126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0
# 
# smallest(209917) --> [29917, 0, 1] or ...
# 
# [29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0] is greater than 
# index `i` in [29917, 0, 1].
# 
# 29917 is the smallest number gotten by taking 2 at index 0 and putting it at index 1 which gave 029917 which is the number 29917.
# 
# smallest(1000000) --> [1, 0, 6] or ...
# 
# Note
# Have a look at "Sample Tests" to see the input and output in each language
# -----------------------------------------------------------

def smallest(n):
    n_digits = len(str(n))
    answer = [n, 0, 0]
    for i in range(1, n_digits + 1):
        for j in range(1, n_digits + 1):
            n_arr = list(str(n))
            digit = int(n_arr[i - 1])
            del n_arr[i - 1]
            n_arr.insert(j - 1, digit)
            new_n = int("".join(str(k) for k in n_arr))
            if new_n < answer[0]:
                answer = [new_n, (i - 1), (j - 1)]
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