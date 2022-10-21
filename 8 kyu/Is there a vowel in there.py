# -----------------------------------------------------------
# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).
# 
# If they are, change the array value to a string of that vowel.
# 
# Return the resulting array.
# -----------------------------------------------------------

def is_vow(inp):
    for i, j in enumerate(inp):
        if chr(j) in "aeiou":
            inp[i] = chr(j)
    return inp

# or

def is_vow(inp):
    return [chr(i) if chr(i) in "aeiou" else i for i in inp]