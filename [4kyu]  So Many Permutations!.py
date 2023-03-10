# https://www.codewars.com/kata/5254ca2719453dcc0b00027d

import itertools

def permutations(s):
    word = ''
    perm_set = itertools.permutations(s)
    for i in perm_set:
        for j in i:
            word += j
        word += ' '
    return list(set(word.split()))