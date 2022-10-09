# -----------------------------------------------------------
# Write a function that returns a string in which firstname is swapped with last name.
# 
# Example(Input --> Output)
# 
# "john McClane" --> "McClane john"
# -----------------------------------------------------------

def name_shuffler(str_):
    arr = str_.split()
    return(arr[1] + " " + arr[0])

# or

def name_shuffler(str_):
    return " ".join(reversed(str_.split()))

# or

def name_shuffler(str_):
    return " ".join(str_.split()[::-1])
