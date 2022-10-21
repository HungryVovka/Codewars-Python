# -----------------------------------------------------------
# Description:
# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
# 
# Examples
# replace("Hi!") === "H!!"
# replace("!Hi! Hi!") === "!H!! H!!"
# replace("aeiou") === "!!!!!"
# replace("ABCDE") === "!BCD!"
# -----------------------------------------------------------

def replace_exclamation(s):
    answer = ("!" if i in "aeiouAEIOU" else i for i in s)
    return "".join(answer)

# or

import re

def replace_exclamation(s):
    return re.sub("[aeiouAEIOU]", "!", s)