# -----------------------------------------------------------
# When provided with a number between 0-9, return it in words.
# 
# Input :: 1
# 
# Output :: "One".
# 
# If your language supports it, try using a switch statement.
# -----------------------------------------------------------

def switch_it_up(number):
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return words[number]