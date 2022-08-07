# -----------------------------------------------------------
# Complete the function which converts a binary number (given as a string) to a decimal number.
# -----------------------------------------------------------

def bin_to_decimal(inp):
    num = 0
    for i in range(len(inp)):
        if inp[i] == "1":
            num += 2 ** (len(inp) - i - 1)
    return num

# or

def bin_to_decimal(inp):
    return int(inp, 2)