# -----------------------------------------------------------
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be 
# capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# 
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# -----------------------------------------------------------

def to_camel_case(text):
    if text == "":
        return ""
    text = text.replace("-", " ")
    text = text.replace("_", " ")
    text = text.split()
    for i in range(1, len(text)):
        text[i] = text[i].capitalize()
    return "".join(text)

# or

import re

def to_camel_case(text):
    if text == "":
        return ""
    text = re.split(r"[-_]", text)
    for i in range(1, len(text)):
        text[i] = text[i].capitalize()
    return "".join(text)