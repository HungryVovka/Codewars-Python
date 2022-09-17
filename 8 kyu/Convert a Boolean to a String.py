# -----------------------------------------------------------
# Implement a function which convert the given boolean value into its string representation.
# 
# Note: Only valid inputs will be given.
# -----------------------------------------------------------

def boolean_to_string(b):
    if b == True:
        return("True")
    if b == False:
        return("False")

# or

def boolean_to_string(b):
    return "True" if b == True else "False"

# or

def boolean_to_string(b):
    return str(b)
