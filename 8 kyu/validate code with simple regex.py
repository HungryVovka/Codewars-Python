# -----------------------------------------------------------
# Basic regex tasks. Write a function that takes in a numeric code of any length. The function should check if the code begins with 1, 2, or 3 and return 
# true if so. Return false otherwise.
# 
# You can assume the input will always be a number.
# -----------------------------------------------------------

def validate_code(code):
    return str(code).startswith("1") or \
        str(code).startswith("2") or \
        str(code).startswith("3")

# or

def validate_code(code):
    return str(code).startswith(("1", "2", "3"))

# or

import re

def validate_code(code):
    return bool(re.match("[123]", str(code)))

# or

def validate_code(code):
    return str(code)[0] in "123"