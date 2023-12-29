# -----------------------------------------------------------
# A category page displays a set number of products per page, with pagination at the bottom allowing the user to move from page to page.
# 
# Given that you know the page you are on, how many products are in the category in total, and how many products are on any given page, how would 
# you output a simple string showing which products you are viewing..
# 
# Examples
# In a category of 30 products with 10 products per page, on page 1 you would see
# 
# 'Showing 1 to 10 of 30 Products.'
# 
# In a category of 26 products with 10 products per page, on page 3 you would see
# 
# 'Showing 21 to 26 of 26 Products.'
# 
# In a category of 8 products with 10 products per page, on page 1 you would see
# 
# 'Showing 1 to 8 of 8 Products.'
# -----------------------------------------------------------

def pagination_text(page_number, page_size, total_products):
    start = (page_number - 1) * page_size + 1
    end = min(page_number * page_size, total_products)
    return f"Showing {start} to {end} of {total_products} Products."

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