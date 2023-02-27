# https://www.codewars.com/kata/5541f58a944b85ce6d00006a

def productFib(prod):
    f,t = 0,1
    while f * t < prod:
        f,t = t, f+t
    return [f,t, f*t==prod]