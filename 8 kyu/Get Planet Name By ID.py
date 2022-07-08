# -----------------------------------------------------------
# The function is not returning the correct values. Can you figure out why?
# 
# Example (Input --> Output ):
# 
# 3 --> "Earth"
# -----------------------------------------------------------

def get_planet_name(id):
    name = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    return name[id-1]