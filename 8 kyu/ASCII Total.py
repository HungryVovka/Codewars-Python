# -----------------------------------------------------------
# You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all ASCII characters.
# 
# examples:
# 
# uniTotal("a") == 97 uniTotal("aaa") == 291
# -----------------------------------------------------------

def uni_total(s):
    total = 0
    s = list(s)
    for i in s:
        total += ord(i)
    return total

# or

def uni_total(s):
    return sum(map(ord, s))

# or

def uni_total(s):
    return sum(ord(i) for i in s)