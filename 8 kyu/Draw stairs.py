# -----------------------------------------------------------
# Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.
# 
# For example n = 3 result in:
# 
# "I\n I\n  I"
# or printed:
# 
# I
#  I
#   I
# Another example, a 7-step stairs should be drawn like this:
# 
# I
#  I
#   I
#    I
#     I
#      I
#       I
# -----------------------------------------------------------

def draw_stairs(n):
    answer = ''
    for s in range (0, n-1):
        answer += ' ' * s + 'I\n'
    answer += ' ' * (n-1) + 'I'
    return answer