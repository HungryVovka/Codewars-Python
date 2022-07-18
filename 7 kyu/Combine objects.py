# -----------------------------------------------------------
# Your task is to write a function that takes two or more objects and returns a new object which combines all the input objects.
# 
# All input object properties will have only numeric values. Objects are combined together so that the values of matching keys are added together.
# 
# An example:
# 
# objA = { 'a': 10, 'b': 20, 'c': 30 }
# objB = { 'a': 3, 'c': 6, 'd': 3 }
# combine(objA, objB) # Returns { a: 13, b: 20, c: 36, d: 3 }
# 
# The combine function should be a good citizen, so should not mutate the input objects.
# -----------------------------------------------------------

def combine(*args):
    combine = {}
    for i in args:
        for j, k in i.items():
            if j in combine:
                combine[j] = combine[j] + k
            else:
                combine[j] = k
    return combine