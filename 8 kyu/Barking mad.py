# -----------------------------------------------------------
# Teach snoopy and scooby doo how to bark using object methods. Currently only snoopy can bark and not scooby doo.
# 
# snoopy.bark() #return "Woof"
# scoobydoo.bark() #undefined
# 
# Use method prototypes to enable all Dogs to bark.
# -----------------------------------------------------------

class Dog():
    def __init__(self, breed):
        self.breed = breed
        self.bark = lambda: "Woof"
    
snoopy, scoobydoo = Dog("Beagle"), Dog("Great Dane")