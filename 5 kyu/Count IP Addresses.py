# -----------------------------------------------------------
# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the 
# last one).
# 
# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.
# 
# Examples
# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246
# -----------------------------------------------------------

def ips_between(start, end):
    start = [int(i) for i in start.split(".")]
    end = [int(j) for j in end.split(".")]
    ip_count = 0
    for k in range(4):
        difference = end[k] - start[k]
        difference *= (256**(3 - k))
        ip_count += difference
    return ip_count

# or

import ipaddress

def ips_between(start, end):
    start = int(ipaddress.ip_address(start))
    end = int(ipaddress.ip_address(end))
    return end - start

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