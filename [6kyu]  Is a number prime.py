# https://www.codewars.com/kata/5262119038c0985a5b00029f

import math


def is_prime(x):
    if x <= 1: return False
    for i in range(2,int(math.sqrt(x))+1):
        if (x%i) == 0:
            return False
    return True
