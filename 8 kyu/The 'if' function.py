# -----------------------------------------------------------
# Create a function called _if which takes 3 arguments: a boolean value bool and 2 functions (which do not take any parameters): func1 and 
# func2
# 
# When bool is truth-ish, func1 should be called, otherwise call the func2.
# 
# Example:
# def truthy(): 
#   print("True")
#  
# def falsey(): 
#   print("False")
#   
# _if(True, truthy, falsey)
# prints 'True' to the console
# -----------------------------------------------------------

def _if(bool, func1, func2):
    if bool == True:
        return func1()
    else:
        return func2()
