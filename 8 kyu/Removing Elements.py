# -----------------------------------------------------------
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
# 
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# 
# None of the arrays will be empty, so you don't have to worry about that!
# -----------------------------------------------------------

def remove_every_other(my_list):
    return [j for i, j in enumerate(my_list) if not i % 2]

# or

def remove_every_other(my_list):
    return my_list[::2]