# -----------------------------------------------------------
# Mr. E Ven only likes even length words. Please create a translator so that he doesn't 
# have to hear those pesky odd length words. For some reason he also hates punctuation, 
# he likes his sentences to flow.
# 
# Your translator should take in a string and output it with all odd length words having 
# an extra letter (the last letter in the word). It should also remove 
# all punctuation (.,?!) as well as any underscores (_).
# 
# "How did we end up here? We go?" translated becomes-> "Howw didd we endd up here We go"
# -----------------------------------------------------------

import re   # sub, findall

def evenator(s: str) -> str:
    # Get rid of those pesky odd length words
    cleaned = re.sub(r"[.,?!_]", "", s)
    words = re.findall(r"[A-Za-z0-9]+", cleaned)
    result_words: list[str] = []
    for c in words:
        if len(c) % 2 != 0:
            c = c + c[-1]
        result_words.append(c)
    return " ".join(result_words)

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