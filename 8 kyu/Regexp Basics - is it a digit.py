# -----------------------------------------------------------
# Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.
# -----------------------------------------------------------

import re
def is_digit(n):
    search = re.search('[\d]', n)
    return search[0] == n if search else False

# or

def is_digit(n):
    return len(n)==1 and n.isdigit()