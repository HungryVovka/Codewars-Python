# -----------------------------------------------------------
# Convert a hash into an array. Nothing more, Nothing less.
# 
# {name: 'Jeremy', age: 24, role: 'Software Engineer'}
# 
# should be converted into
# 
# [["age", 24], ["name", "Jeremy"], ["role", "Software Engineer"]]
# 
# Note: The output array should be sorted alphabetically by key name.
# 
# Good Luck!
# -----------------------------------------------------------

def convert_hash_to_array(hash):
    return sorted(map(list, hash.items()))

# or

def convert_hash_to_array(hash):
    return sorted(list(h) for h in hash.items())

# or

def convert_hash_to_array(hash):
    return [[h, hash[h]] for h in sorted(hash)]