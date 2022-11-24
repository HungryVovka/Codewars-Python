# -----------------------------------------------------------
# Given a string of numbers, you must perform a method in which you will translate this string into text, following the next image.
# 
# for example if you get 22 you will b, if you get 222 you will return c. if you get 2222 return ca
# 
# Here some samples:
# 
# 443355555566604466690277733099966688 -> hello how are you., 55282 -> kata.
# 
# 1 is used to separate letters with the same number.
# 
# always transform the number to the letter with the maximum value, as long as it does not have a 1 in the middle.
# 
# 777777 = "sq". 7717777 = "qs".
# 
# you cant return numbers.
# 
# 0 are spaces in the string.
# 
# Given a empty string, return empty string.
# 
# Return a lowercase string.
# -----------------------------------------------------------

def phone_words(string_of_nums):
    if string_of_nums == "":
        return string_of_nums
    return string_of_nums.replace("9999", "z")\
                    .replace("999", "y").replace("99", "x").replace("9", "w")\
                    .replace("888", "v").replace("88", "u").replace("8", "t")\
                    .replace("7777", "s")\
                    .replace("777", "r").replace("77", "q").replace("7", "p")\
                    .replace("666", "o").replace("66", "n").replace("6", "m")\
                    .replace("555", "l").replace("55", "k").replace("5", "j")\
                    .replace("444", "i").replace("44", "h").replace("4", "g")\
                    .replace("333", "f").replace("33", "e").replace("3", "d")\
                    .replace("222", "c").replace("22", "b").replace("2", "a")\
                    .replace("1", "").replace("0", " ")