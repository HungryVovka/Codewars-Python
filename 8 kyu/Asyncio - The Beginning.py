# -----------------------------------------------------------
# Story
# As you walk the streets with your crush beside you, you are thinking about the world and how everything works... Wait!! Your crush? Shit, you are 
# dreaming again.
# 
# Task
# Now implement a coroutine dreaming which sleeps for n seconds and then returns m ** n without entirely blocking the execution of other 
# coroutines that might be running.
# 
# Note
# 0 < n < 7
# 
# 0 < m < 100
# -----------------------------------------------------------

from asyncio import sleep

def dreaming(n, m):
    return sleep(n, m**n) 