# -----------------------------------------------------------
# Task
# You are given a dictionary/hash/object containing some languages and your test results in the given languages. Return the list of languages where 
# your test score is at least 60, in descending order of the results.
# 
# Note: the scores will always be unique (so no duplicate values)
# 
# Examples
# {"Java": 10, "Ruby": 80, "Python": 65}    -->  ["Ruby", "Python"]
# {"Hindi": 60, "Dutch" : 93, "Greek": 71}  -->  ["Dutch", "Greek", "Hindi"]
# {"C++": 50, "ASM": 10, "Haskell": 20}     -->  []
# 
# My other katas
# If you enjoyed this kata then please try my other katas! :-)
# 
# Translations are welcome!
# -----------------------------------------------------------

def my_languages(results):
    return sorted([i for i, j in results.items() if j >= 60], key = lambda x: results[x], reverse = True)

# or

def my_languages(results):
    return sorted((i for i, j in results.items() if j >= 60), key = results.get, reverse = True)