# -----------------------------------------------------------
# Structural Pattern Matching:
# NOTE: Make Sure You Select Python 3.10 for Structural Pattern Matching.
# 
# Read PEP 636 (https://peps.python.org/pep-0636/) may help you understand it.
# 
# This Kata is made to practice the Structural Pattern Matching.
# 
# Examples of Structural Pattern Matching:
# There is some special things in Structural Pattern Matching:
# 
# You can match with sequence, or, guard, mapping, using as,etc. Not just a replacement of if ... elif ... elif ... else, full details are in 
# PEP636.
# 
# Examples
# 
# match [1, 2, 3]:
#     case [x, y, z]:
#         print(x) # This would print: 1
#         print(y) # This would print: 2
#         print(z) # This would print: 3
# 
# 
# # Different item to match, but it would not match the same pattern above.
# match '123':
#     case [x, y, z]:
#         # This wouldn't match.
#     case _:
#         print(False) # This would match.
# 
# 
# # another example
# match ['item0', 'item1', 'item2', 'item3']:
#     case [*x, y]:
#         print(', '.join(x) + ' and ' + y) # This would print: item0, item1, item2 and item3
# 
# Pluspoint of Structural Pattern Matching:
# From PEP635 (https://peps.python.org/pep-0636/):
# 
# (This is just part of it, read PEP635 will give you full understanding of it.)
# 
# The if ... elif ... elif ... else idiom is often used to find out the type or shape of an object in an ad-hoc fashion, using one or more checks like 
# isinstance(x, cls), hasattr(x, "attr"), len(x) == n or "key" in x as guards to select an applicable block. The block can then assume x supports the 
# interface checked by the guard. For example:
# 
# if isinstance(x, tuple) and len(x) == 2:
#     host, port = x
#     mode = "http"
# elif isinstance(x, tuple) and len(x) == 3:
#     host, port, mode = x
# # Etc.
# 
# Code like this is more elegantly rendered using match:
# 
# match x:
#     case host, port:
#         mode = "http"
#     case host, port, mode:
#         pass
#     # Etc.
# 
# Task:
# You will get an arg which consists only of 0, 1, 2, 3, '0', '1', '2', '3' (or none of them).
# 
# arg will be a string or list.
# 
# Return the result with the following rules:
# 
# If arg is an empty list, return 0
# 
# If arg is a list with 1 element, convert the element to integer if not yet an integer, then return it.
# 
# If arg is a list with 2 or more elements, convert the first and last elements to integer if not yet integers, then return 
# first element divided by the last element (float division).
# 
# If divided by 0 or arg is not a list, return None.
# 
# Examples (arg --> output)
# ('') --> None
# ([]) --> 0
# (['2']) --> 2
# ([0]) --> 0
# ([3, 1, '2']) --> 1.5
# ('123') --> None
# (['0', 0]) --> None
# (['0', 2, '3']) --> 0.0
# -----------------------------------------------------------

def matching(arg):
    match arg:
        case []:
            return 0
        case [a]:
            return int(a)
        case [a, *_, an] if int(an) != 0:
            return int(a) / int(an)
        case _:
            return None