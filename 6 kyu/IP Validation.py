# -----------------------------------------------------------
# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with 
# values between 0 and 255, inclusive.
# 
# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# 
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# 
# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string
# -----------------------------------------------------------

def is_valid_IP(strng):
    octets = strng.split(".")
    if len(octets) != 4:
        return False
    for i in octets:
        if " " in i or (len(i) > 1 and i.startswith("0")) or not i.isdecimal():
            return False
    return all((int(i) >= 0 and int(i) <= 255) for i in octets)

# or

import re

def is_valid_IP(strng):
    validation = r"^(\d{1,3}\.){3}\d{1,3}$"
    if re.match(validation, strng):
        octets = strng.split(".")
        check1 = all((str(int(i)) == i) for i in octets)
        check2 = all((int(i) >= 0 and int(i) <= 255) for i in octets)
        return check1 and check2
    return False

# or

import socket

def is_valid_IP(strng):
    try:
        socket.inet_pton(socket.AF_INET, strng)
        return True
    except (socket.error):
        return False

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