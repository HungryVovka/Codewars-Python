# -----------------------------------------------------------
# Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health 
# can't be less than 0.
# -----------------------------------------------------------

def combat(health, damage):
    if health < damage:
        return 0
    return health - damage

# or

def combat(health, damage):
    return 0 if health < damage else health - damage

# or

def combat(health, damage):
    return max(health - damage, 0)