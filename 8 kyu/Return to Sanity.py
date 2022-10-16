# -----------------------------------------------------------
# This function should return an object, but it's not doing what's intended. What's wrong?
# -----------------------------------------------------------

def mystery():
    results = {
        'sanity': 'Hello',
    }
    return results

# or

def mystery():
    results = {
        'sanity': 'Hello',
    }
    return \
    results

# or

def mystery(return_to_sanity = {"sanity" : "Hello"}):
    return return_to_sanity