# -----------------------------------------------------------
# The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.
# 
# The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each 
# incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).
# 
# If the score < 0, return 0.
# 
# For example:
# 
# checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
# checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
# checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
# checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
# -----------------------------------------------------------

def check_exam(arr1, arr2):
    i = 0
    score = 0
    while i < len(arr1):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr2[i] == "":
            score += 0
        else:
            score -= 1
        i += 1
    return score if score >= 0 else 0

# or

def check_exam(arr1, arr2):
    score = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr2[i] == "":
            score += 0
        else:
            score -= 1
        i += 1
    return score if score >= 0 else 0

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