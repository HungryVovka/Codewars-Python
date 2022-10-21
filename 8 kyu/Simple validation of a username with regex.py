# -----------------------------------------------------------
# Write a simple regex to validate a username. Allowed characters are:
# 
# lowercase letters,
# numbers,
# underscore
# 
# Length should be between 4 and 16 characters (both included).
# -----------------------------------------------------------

def validate_usr(username):
    if 16 < len(username) or len(username) < 4:
        return False
    valid = "0123456789_abcdefghijklmnopqrstuvwxyz"
    for i in username:
        if i not in valid:
            return False
    return True

# or

def validate_usr(username):
    valid = "0123456789_abcdefghijklmnopqrstuvwxyz"
    if 16 >= len(username) >= 4 and all (i in valid for i in username):
        return True
    return False

# or

import re

def validate_usr(username):
    return re.match(r"^[0-9_a-z]{4,16}$", username) is not None