import re


def to_camel_case(text):
    strok = list(text)
    result = ""
    for i in range(len(strok)):
        print(text[i])
        if strok[i] == "_":
            strok[i] = text[i+1].upper()
            result += strok[i]
            strok[i+1] = " "   
        elif strok[i] == "-":
            strok[i] = text[i+1].upper()
            result += strok[i]
            strok[i+1] = " " 
        elif strok[i] == " ":
            pass
        else:
            result += strok[i]
    return result
    