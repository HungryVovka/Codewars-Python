# -----------------------------------------------------------
# What is the answer to life the universe and everything
# 
# Create a function that will make anything true
# 
#     anything({}) != [],          'True'
#     anything('Hello') < 'World', 'True'
#     anything(80) > 81,           'True'
#     anything(re) >= re,          'True'
#     anything(re) <= math,        'True'
#     anything(5) == ord,          'True'
# 
# Source: CheckIO (https://py.checkio.org/ru/mission/solution-for-anything/)
# -----------------------------------------------------------

class anything:
    def __init__(self, any):
        pass
    
    def __eq__(self, any):
        return True
    
    def __ge__(self, any):
        return True
    
    def __gt__(self, any):
        return True 
    
    def __le__(self, any):
        return True
    
    def __lt__(self, any):
        return True
    
    def __ne__(self, any):
        return True

# or

class anything:
    def __init__(self, any):
        pass
    
    def __eq__(self, any):
        return True
    
    __ge__ = __gt__ = __le__ = __lt__ = __ne__ = __eq__

# or

class anything(str):
    __eq__ = __ge__ = __gt__ = __le__ = __lt__ = __ne__ = str