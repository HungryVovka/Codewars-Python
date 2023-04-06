# -----------------------------------------------------------
# Ready! Set! Fire... but where should you fire?
# 
# The battlefield is 3x3 wide grid. HQ has already provided you with an array for easier computing:
# 
# grid = ['top left',    'top middle',    'top right',
#         'middle left', 'center',        'middle right',
#         'bottom left', 'bottom middle', 'bottom right']
# 
# HQ radios you with 'x' and 'y' coordinates. x=0 y=0 being 'top left' part of the battlefield;
# 
# Your duty is to create a function that takes those Xs and Ys and return the correct grid sector to be hit.
# 
# fire(0,0) # 'top left'
# fire(1,2) # 'bottom middle'
# etc.
# 
# Notice the grid is a monodimensional array, good luck!
# -----------------------------------------------------------

grid = ["top left", "top middle", "top right", 
        "middle left", "center", "middle right",
        "bottom left", "bottom middle", "bottom right"]

def fire(x,y):
    return grid[x + y * 3]

# or

def fire(x,y):
    grid = [["top left", "top middle", "top right"], 
            ["middle left", "center", "middle right"],
            ["bottom left", "bottom middle", "bottom right"]]
    return grid[y][x]

# -----------------------------------------------------------
# License
# Tasks are the property of Codewars (https://www.codewars.com/) 
# and users of this resource.
# 
# All solution code in this repository 
# is the personal property of Vladimir Rukavishnikov
# (vladimirrukavishnikovmail@gmail.com).
# 
# Copyright (C) 2022 Vladimir Rukavishnikov
# 
# This file is part of the HungryVovka/Codewars-Python
# (https://github.com/HungryVovka/Codewars-Python)
# 
# License is GNU General Public License v3.0
# (https://github.com/HungryVovka/Codewars-Python/blob/main/LICENSE.md)
# 
# You should have received a copy of the GNU General Public License v3.0
# along with this code. If not, see http://www.gnu.org/licenses/
# -----------------------------------------------------------