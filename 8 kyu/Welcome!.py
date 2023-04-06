# -----------------------------------------------------------
# Your start-up's BA has told marketing that your website has a large audience in Scandinavia and surrounding countries. Marketing thinks it would be 
# great to welcome visitors to the site in their own language. Luckily you already use an API that detects the user's location, so this is an easy win.
# 
# The Task
# Think of a way to store the languages as a database (eg an object). The languages are listed below so you can copy and paste!
# Write a 'welcome' function that takes a parameter 'language' (always a string), and returns a greeting - if you have it in your database. It should 
# default to English if the language is not in the database, or in the event of an invalid input.
# 
# The Database
# 'english': 'Welcome',
# 'czech': 'Vitejte',
# 'danish': 'Velkomst',
# 'dutch': 'Welkom',
# 'estonian': 'Tere tulemast',
# 'finnish': 'Tervetuloa',
# 'flemish': 'Welgekomen',
# 'french': 'Bienvenue',
# 'german': 'Willkommen',
# 'irish': 'Failte',
# 'italian': 'Benvenuto',
# 'latvian': 'Gaidits',
# 'lithuanian': 'Laukiamas',
# 'polish': 'Witamy',
# 'spanish': 'Bienvenido',
# 'swedish': 'Valkommen',
# 'welsh': 'Croeso'
# 
# Possible invalid inputs include:
# 
# IP_ADDRESS_INVALID - not a valid ipv4 or ipv6 ip address
# IP_ADDRESS_NOT_FOUND - ip address not in the database
# IP_ADDRESS_REQUIRED - no ip address was supplied
# -----------------------------------------------------------

def greet(language):
    welcome = {'english': 'Welcome',
     'czech': 'Vitejte',
     'danish': 'Velkomst',
     'dutch': 'Welkom',
     'estonian': 'Tere tulemast',
     'finnish': 'Tervetuloa',
     'flemish': 'Welgekomen',
     'french': 'Bienvenue',
     'german': 'Willkommen',
     'irish': 'Failte',
     'italian': 'Benvenuto',
     'latvian': 'Gaidits',
     'lithuanian': 'Laukiamas',
     'polish': 'Witamy',
     'spanish': 'Bienvenido',
     'swedish': 'Valkommen',
     'welsh': 'Croeso',
    }
    try:
        return welcome[language]
    except KeyError:
        return 'Welcome'

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