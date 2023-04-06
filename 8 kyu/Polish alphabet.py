# -----------------------------------------------------------
# There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.
# 
# Your task is to change the letters with diacritics:
# 
# ą -> a,
# ć -> c,
# ę -> e,
# ł -> l,
# ń -> n,
# ó -> o,
# ś -> s,
# ź -> z,
# ż -> z
# 
# and print out the string without the use of the Polish letters.
# 
# For example:
# 
# "Jędrzej Błądziński"  -->  "Jedrzej Bladzinski"
# -----------------------------------------------------------

def correct_polish_letters(st):
    diactritic = {
        "ą" : "a",
        "ć" : "c",
        "ę" : "e",
        "ł" : "l",
        "ń" : "n",
        "ó" : "o",
        "ś" : "s",
        "ź" : "z",
        "ż" : "z",
    }
    return "".join(diactritic[i] if i in diactritic else \
                  i for i in st)

# or

def correct_polish_letters(st):
    return st.translate(st.maketrans("ąćęłńóśźż", "acelnoszz"))

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