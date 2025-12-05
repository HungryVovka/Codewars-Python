# -----------------------------------------------------------
# ECB (European Central Bank) needs your help! They have noticed that fake Euro bills have been 
# spreading over because of the rogues.
# 
# There are some advanced techniques to determine if the bill was hand-made or not. But there is a 
# specific algorithm for Euro bills (though, I can't find any proofs of it but every single Euro 
# bill I have seen, follows this algorithm. For the purpose of this task, we will suppose that 
# this algorithm is totally true). Your task is to validate the Euro bill based on its 
# serial number. Assume that every other detail of the bill is either real or perfectly 
# made by the rogues.
# 
# Here is the algorithm:
# 
# The serial number of every Euro bill contains 2 uppercase latin letters at the start and 
# the following 10 digits.
# 
# 1. Sum every digit in a serial number.
# 2. Get the English Alphabetical position of the two letters. (A - 1, B - 2, C - 3 and etc.).
# 3. Add those numbers to the already existing sum of digits.
# 4. Sum the result's digits up. If the sum is not 1-digit number, keep summing the new number's digits, until the result is 1-digit number.
# 
# If the eventual result equals 7, you're holding a real Euro bill. Otherwise, the bill is fake. 
# Assume that every input matches the requirements of a serial number (2 uppercase latin letters and 10 digits).
# 
# 
# An example of a valid serial number:
# 
# VA0436214792
# V = 22; A = 1
# 
# 22 + 1 + 0 + 4 + 3 + 6 + 2 + 1 + 4 + 7 + 9 + 2 = 61 -> 6 + 1 = 7 -> True
# 
# And an invalid one:
# 
# WF9804350654
# W = 23; F = 6
# 
# 23 + 6 + 9 + 8 + 0 + 4 + 3 + 5 + 0 + 6 + 5 + 4 = 73 -> 10 -> 1 -> False
# 
# Good luck!
# -----------------------------------------------------------

import re   # fullmatch

def validate_euro(serial_number: str) -> bool:
    match_result = re.fullmatch(r"([A-Z]{2})(\d{10})", serial_number)
    if not match_result:
        return False
    letter_part = match_result.group(1)
    digit_part = match_result.group(2)
    digits_sum = sum(int(single_digit) for single_digit in digit_part)
    first_letter_value = ord(letter_part[0]) - ord('A') + 1
    second_letter_value = ord(letter_part[1]) - ord('A') + 1
    total_sum = digits_sum + first_letter_value + second_letter_value
    while total_sum >= 10:
        new_sum = 0
        for single_char in str(total_sum):
            new_sum += int(single_char)
        total_sum = new_sum
    return total_sum == 7

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