# -----------------------------------------------------------
# Write a function that checks if a given string (case insensitive) is a palindrome (https://en.wikipedia.org/wiki/Palindrome).
# -----------------------------------------------------------

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]