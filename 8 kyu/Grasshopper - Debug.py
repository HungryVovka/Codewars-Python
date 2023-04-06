# -----------------------------------------------------------
# Debug celsius converter
# Your friend is traveling abroad to the United States so he wrote a program to convert fahrenheit to celsius. Unfortunately his code has some bugs.
# 
# Find the errors in the code to get the celsius converter working properly.
# 
# To convert fahrenheit to celsius:
# 
# celsius = (fahrenheit - 32) * (5/9)
# 
# Remember that typically temperatures in the current weather conditions are given in whole numbers. It is possible for temperature sensors to 
# report temperatures with a higher accuracy such as to the nearest tenth. Instrument error though makes this sort of accuracy unreliable for many 
# types of temperature measuring sensors.
# -----------------------------------------------------------

def weather_info (temp):
    c = convert_to_celsius(temp)
    if c <= 0:
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convert_to_celsius (temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius

# or

def weather_info (temp):
    c = (temp - 32) * (5 / 9)
    if c > 0:
        return "{} is above freezing temperature".format(c)
    else:
        return "{} is freezing temperature".format(c)

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