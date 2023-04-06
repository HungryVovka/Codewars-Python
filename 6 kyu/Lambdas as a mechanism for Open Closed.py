# -----------------------------------------------------------
# Open/Closed Principle
# The open/closed principle states that code should be closed for modification, yet open for extension. That means you should be able to add new 
# functionality to an object or method without altering it.
# 
# One way to achieve this is by using a lambda, which by nature is lazily bound to the lexical context. Until you call a lambda, it is just a piece of data 
# you can pass around.
# 
# Task at hand
# Implement 3 lambdas that alter a message based on emotoion:
# 
# spoken    = lambda greeting: ??? # "Hello."
# shouted   = lambda greeting: ??? # "HELLO!"
# whispered = lambda greeting: ??? # "hello."
# 
# Then create a fourth lambda, this one will take one of the above lambdas and a message, and the last lambda will delegate the emotion and the 
# message up the chain.
# 
# greet = lambda style, msg: ???
# -----------------------------------------------------------

spoken    = lambda greeting: greeting.capitalize() + "."
shouted   = lambda greeting: greeting.upper() + "!"
whispered = lambda greeting: greeting.lower() + "."

greet = lambda style, msg: style(msg)

# or

spoken    = lambda greeting: greeting.title() + "."
shouted   = lambda greeting: greeting.upper() + "!"
whispered = lambda greeting: greeting.lower() + "."

greet = lambda style, msg: style(msg)

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