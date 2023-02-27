# https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    if r < 0 or g < 0 or b < 0:
        rgbi = ["00" if i < 0 else "{:02x}".format(min(i,255)).upper() for i in [r,g,b]]
        return "".join(rgbi)        
    else:
        return "{:02x}{:02x}{:02x}".format(min(r,255),min(g,255),min(b,255)).upper()