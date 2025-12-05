# -----------------------------------------------------------
# Implement function createTemplate which takes string with tags wrapped in 
# {{brackets}} as input and returns closure, which can fill string with data 
# (flat object, where keys are tag names).
# 
# template = create_template("{{name}} likes {{animalType}}")
# template(name="John", animalType="dogs") # John likes dogs
# 
# When key doesn't exist in the map, put there empty string.
# -----------------------------------------------------------

import re   # compile, sub

def create_template(template: str) -> object:
    tag_pattern = re.compile(r"{{\s*([A-Za-z_][A-Za-z0-9_]*)\s*}}")
    
    def filler(**data: str) -> str:
        def replace_tag(match) -> object:
            tag_name = match.group(1)
            return data.get(tag_name, "")
        
        return tag_pattern.sub(replace_tag, template)
    return filler

# -----------------------------------------------------------
# License
# Tasks are the property of Codewars (https://www.codewars.com/) 
# and users of this resource.
# 
# All solution code in this repository 
# is the personal property of Vladimir Rukavishnikov
# (vladimirrukavishnikovmail@gmail.com).
# 
# Copyright (C) 2025 Vladimir Rukavishnikov
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