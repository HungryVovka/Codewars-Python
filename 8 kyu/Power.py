# -----------------------------------------------------------
# The goal is to create a function of two inputs number and power, that "raises" the number up to power (ie multiplies number by itself power 
# times).
# 
# Examples
# number_to_pwr(3, 2)  # -> 9 ( = 3 * 3 )
# number_to_pwr(2, 3)  # -> 8 ( = 2 * 2 * 2 )
# number_to_pwr(10, 6) # -> 1000000
# 
# Note: math.pow and some others math functions are disabled on final tests.
# -----------------------------------------------------------

def number_to_pwr(number, p):
    i, j = 1, 1
    while j <= p:
        i *= number
        j += 1
    return i