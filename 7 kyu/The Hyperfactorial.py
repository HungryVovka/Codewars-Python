# -----------------------------------------------------------
# Description
# In mathematics, and more specifically number theory, the hyperfactorial of a positive integer n is the product of the numbers 1^1, 2^2, ...,n^n:
# H(n) = 1^1 * 2^2 * 3^3 * ... * (n - 1)^(n - 1) * n^n
# H(n) = П(i = 1)^n i^i
# 
# Check out this Wikipedia article for more detail
# 
# Your task
# Implement a function hyperfact(num) that takes a positive integer num and returns the hyperfactorial of it.
# 
# In order for your answer not to be too messy (hyperfactorial of 100 is 9015 digits long) give the answer modulo 1000000007.
# 
# Notes
# 1 <= n <= 300
# 
# 50 random tests
# -----------------------------------------------------------

def hyperfact(num):
    modulo = int(1e9 + 7)
    answer = 1
    for i in range(1, num + 1):
        answer *= i**i
    return answer % modulo

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