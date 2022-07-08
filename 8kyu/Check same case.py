# -----------------------------------------------------------
# Write a function that will check if two given characters are the same case.
# 
# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0
# 
# Examples
# 'a' and 'g' returns 1
# 
# 'A' and 'C' returns 1
# 
# 'b' and 'G' returns 0
# 
# 'B' and 'g' returns 0
# 
# '0' and '?' returns -1
# -----------------------------------------------------------

cap_let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low_let = []
for c in cap_let:
    low_let.append(c.lower())

def same_case(a, b):
    if a in cap_let and b in cap_let:
        return(1)
    if a in low_let and b in low_let:
        return(1)
    if (a in cap_let and b in low_let) or (a in low_let and b in cap_let):
        return(0)
    if (a not in cap_let and a not in low_let) or (b not in cap_let and b not in low_let):
        return(-1)