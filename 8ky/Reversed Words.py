# -----------------------------------------------------------
# Complete the solution so that it reverses all of the words within the string passed in.
# 
# Example(Input --> Output):
# 
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
# -----------------------------------------------------------

def reverse_words(s):
    s = s.split()
    s.reverse()
    s = " ".join(s)
    return s

# or

def reverse_words(s):
    separator = " "
    return separator.join(reversed(s.split(separator)))