# -----------------------------------------------------------
# There is a bus moving in the city, and it takes and drop some people in each bus stop.
# 
# You are provided with a list (or array) of integer pairs. Elements of each pair represent number of people get into bus (The first item) and number of 
# people get off the bus (The second item) in a bus stop.
# 
# Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the 
# bus is not empty and some people are still in the bus, and they are probably sleeping there :D
# 
# Take a look on the test cases.
# 
# Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.
# 
# The second value in the first integer array is 0, since the bus is empty in the first bus stop.
# -----------------------------------------------------------

def number(bus_stops):
    leftinbus = [i[0] - i[1] for i in bus_stops]
    return sum(leftinbus)

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