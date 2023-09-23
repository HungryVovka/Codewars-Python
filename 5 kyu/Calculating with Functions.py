# -----------------------------------------------------------
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
# 
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# 
# Requirements:
# 
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# 
# eight(divided_by(three()))
# -----------------------------------------------------------

class Calculator:
    def zero(self, x=None): return x(0) if x else 0
    def one(self, x=None): return x(1) if x else 1
    def two(self, x=None): return x(2) if x else 2
    def three(self, x=None): return x(3) if x else 3
    def four(self, x=None): return x(4) if x else 4
    def five(self, x=None): return x(5) if x else 5
    def six(self, x=None): return x(6) if x else 6
    def seven(self, x=None): return x(7) if x else 7
    def eight(self, x=None): return x(8) if x else 8
    def nine(self, x=None): return x(9) if x else 9
    
    @staticmethod
    def plus(b):
        def add(a): return a + b
        return add
    
    @staticmethod
    def minus(b):
        def substract(a): return a - b
        return substract
    
    @staticmethod
    def times(b):
        def multiply(a): return a * b
        return multiply
    
    @staticmethod
    def divided_by(b):
        def divide(a):
            try:
                return int(a / b)
            except:
                return 0
        return divide
    
calc = Calculator()

zero, one, two, three, four, five, six, seven, eight, nine = \
calc.zero, calc.one, calc.two, calc.three, calc.four, \
calc.five, calc.six, calc.seven, calc.eight, calc.nine

plus = Calculator.plus
minus = Calculator.minus
times = Calculator.times
divided_by = Calculator.divided_by

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