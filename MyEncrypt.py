def MyEncrypt(x):
    newstring = ""
    for ch in x:
        #print (ch, ord(ch))
        y = ord(ch) + 5
        newstring = newstring + chr(y)
    return newstring


print(MyEncrypt("Hello my name is Alicia."))


def MyDecrypt(x):
    newstring = ""
    for ch in x:
        #print (ch, ord(ch))
        y = ord(ch) - 5
        newstring = newstring + chr(y)
    return newstring

print(MyDecrypt("Mjqqt%r~%sfrj%nx%Fqnhnf3"))
