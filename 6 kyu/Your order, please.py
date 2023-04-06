# -----------------------------------------------------------
# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
# 
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# 
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
# 
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""
# -----------------------------------------------------------

def order(sentence):
    arr = []
    dic = {}
    sent_sp = sentence.split(" ")
    for word in sent_sp:
        for letter in word:
            l_alph = ord(letter)
            if l_alph >= ord("0") and l_alph <= ord("9"):
                dic[letter] = sent_sp.index(word)
                arr.append(l_alph - ord("0"))
                break
    arr.sort()
    answer = []
    for i in arr:
        answer.append(sent_sp[dic[str(i)]])
    return " ".join(word for word in answer)

# or

def order(sentence):
    sent_spl = sentence.split()
    return " ".join(sorted(sent_spl, key = min))

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