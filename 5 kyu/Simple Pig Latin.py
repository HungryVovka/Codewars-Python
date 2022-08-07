# -----------------------------------------------------------
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# 
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !
# -----------------------------------------------------------

def pig_it(text):
    arr = text.split()
    answer = []
    for i in arr:
        if i.isalpha():
            answer.append(i[1:] + i[0] + "ay")
        else:
            answer.append(i)
    return " ".join(answer)
