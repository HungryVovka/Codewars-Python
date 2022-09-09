# -----------------------------------------------------------
# Safen User Input Part I - htmlspecialchars
# You are a(n) novice/average/experienced/professional/world-famous Web Developer (choose one) who owns a(n) 
# simple/clean/slick/beautiful/complicated/professional/business website (choose one or more) which contains form fields so visitors can send emails 
# or leave a comment on your website with ease. However, with ease comes danger. Every now and then, a hacker visits your website and attempts to 
# compromise it through the use of XSS (Cross Site Scripting). This is done by injecting script tags into the website through form fields which may 
# contain malicious code (e.g. a redirection to a malicious website that steals personal information).
# 
# Mission
# Your mission is to implement a function that converts the following potentially harmful characters:
# 
# < --> &lt;
# > --> &gt;
# " --> &quot;
# & --> &amp;
# 
# Good luck :D
# -----------------------------------------------------------

def html_special_chars(data):
    data = data.replace("&", "&amp;")
    data = data.replace("<", "&lt;")
    data = data.replace(">", "&gt;")
    data = data.replace('"', "&quot;")
    return data

# or

def html_special_chars(data):
    return data\
        .replace("&", "&amp;")\
        .replace("<", "&lt;")\
        .replace(">", "&gt;")\
        .replace('"', "&quot;")

# or

def html_special_chars(data):
    convert = {'<': '&lt;',
               '>': '&gt;',
               '"': '&quot;',
               '&': '&amp;',
              }
    return "".join(convert.get(i, i) for i in data)