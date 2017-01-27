"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""

def AnyString(x):
    newstring = ""
    x = x.lower()
    for ch in x:
        if ord(ch) is 97:
            newstring = newstring + '*'
        elif ord(ch) is 101:
            newstring = newstring + '^'
        elif ord(ch) is 105:
            newstring = newstring + '%'
        elif ord(ch) is 111:
            newstring = newstring + '$'
        elif ord(ch) is 117:
            newstring = newstring + '?'
        else:
            newstring = newstring + ch
    return newstring

print(AnyString("Alicia Bethany Thoe"))
