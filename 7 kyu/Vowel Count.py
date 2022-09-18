# -----------------------------------------------------------
# Return the number (count) of vowels in the given string.
# 
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# 
# The input string will only consist of lower case letters and/or spaces.
# -----------------------------------------------------------

def get_count(sentence):
    vowels = 0
    for i in sentence:
        if i in "aeiouAEIOU":
            vowels = vowels + 1
    return vowels

# or

def get_count(sentence):
    return sum(i in "aeiouAEIOU" for i in sentence)
