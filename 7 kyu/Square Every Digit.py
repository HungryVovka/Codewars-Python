# -----------------------------------------------------------
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# 
# For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 8^1 and 1^2 is 1.
# 
# Note: The function accepts an integer and returns an integer
# -----------------------------------------------------------

def square_digits(num):
    answer = ''
    numbers = list(str(num))
    for n in numbers:
        answer += str(int(n)*int(n))
    return int(answer)