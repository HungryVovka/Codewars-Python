# -----------------------------------------------------------
# You probably know that number 42 is "the answer to life, the universe and everything" according to Douglas Adams' "The Hitchhiker's Guide to the 
# Galaxy". For Freud, the answer was quite different...
# 
# In the society he lived in, people - women in particular - had to repress their sexual needs and desires. This was simply how the society was at the 
# time. Freud then wanted to study the illnesses created by this, and so he digged to the root of their desires. This led to some of the most important 
# psychoanalytic theories to this day, Freud being the father of psychoanalysis.
# 
# Now, basically, when a person hears about Freud, s/he hears "sex" because for Freud, everything was related to, and explained by sex.
# 
# In this kata, the function will take a string as its argument, and return a string with every word replaced by the explanation to everything, according 
# to Freud. Note that an empty string, or no arguments, should return an empty string.
# -----------------------------------------------------------

def to_freud(sentence):
    arr = sentence.split()
    if len(arr) == 1:
        return("sex")
    if len(arr) > 1:
        return("sex" + " sex" * (len(arr) -1))
    if len(arr) == 0:
        return("")

# or

def to_freud(sentence):
    return (len(sentence.split()) * "sex ").rstrip()

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