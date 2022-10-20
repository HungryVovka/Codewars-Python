# -----------------------------------------------------------
# Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false.
# -----------------------------------------------------------

include = list.__contains__

# or

def include(arr, item):
    return item in arr