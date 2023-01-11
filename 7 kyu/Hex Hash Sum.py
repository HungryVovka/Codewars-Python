# -----------------------------------------------------------
# Complete the function that accepts a valid string and returns an integer.
# 
# Wait, that would be too easy! Every character of the string should be converted to the hex value of its ascii code, then the result should be the sum of 
# the numbers in the hex strings (ignore letters).
# 
# Examples
# "Yo" ==> "59 6f" ==> 5 + 9 + 6 = 20
# "Hello, World!"  ==> 91
# "Forty4Three"    ==> 113
# -----------------------------------------------------------

def hex_hash(code):
    return sum(map(int, filter(str.isdigit, code.encode().hex())))

# or

def hex_hash(code):
    return sum(int(y) for x in code for y in hex(ord(x)) if y.isnumeric())