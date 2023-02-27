# -----------------------------------------------------------
# In this kata, you need to write a function that takes a string and a letter as input and then returns the index of the second occurrence of that letter in 
# the string. If there is no such letter in the string, then the function should return -1. If the letter occurs only once in the string, then -1 should also be 
# returned.
# 
# Examples:
# 
# second_symbol('Hello world!!!','l') --> 3
# second_symbol('Hello world!!!', 'A') --> -1
# 
# Good luck ;) And don't forget to rate this Kata if you liked it.
# -----------------------------------------------------------

def second_symbol(s, symbol):
    i = 0
    for a, b in enumerate(s):
        if b == symbol:
            if i == 1:
                return a
            else:
                i += 1
    return -1

# or

def second_symbol(s, symbol):
    first = s.find(symbol)
    return s.find(symbol, first + 1)