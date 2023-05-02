# -----------------------------------------------------------
# A format for expressing an ordered list of integers is to use a comma separated list of either
# 
# individual integers
# 
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in 
# the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# 
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
# 
# Example:
# 
# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
# 
# Courtesy of rosettacode.org
# -----------------------------------------------------------

def solution(args):
    answer = []
    i = 0
    while i < len(args):
        start = args[i]
        end = start
        while i < len(args) - 1 and args[i + 1] == end + 1:
            end = args[i + 1]
            i += 1
        if start == end:
            answer.append(str(start))
        elif end - start == 1:
            answer.append("{},{}".format(start, end))
        else:
            answer.append("{}-{}".format(start, end))
        i += 1
    return ",".join(answer)

# or

def solution(args):
    answer = ""
    while len(args) > 0:
        start = args.pop(0)
        end = start
        while len(args) > 0 and args[0] == end + 1:
            end = args.pop(0)
        if start == end:
            answer += "%d," % (start)
        elif end - start == 1:
            answer += "%d,%d," % (start, end)
        else:
            answer += "%d-%d," % (start, end)
    return answer[:-1]

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