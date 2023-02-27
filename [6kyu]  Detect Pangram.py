# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())