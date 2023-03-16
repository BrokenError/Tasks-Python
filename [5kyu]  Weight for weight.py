# https://www.codewars.com/kata/55c6126177c9441a570000cc

def order_weight(strng):
    weight = sorted(sorted(strng.split()), key=summa)
    return ' '.join(weight)

def summa(s):
    return sum([int(i) for i in s])