# https://www.codewars.com/kata/54d81488b981293527000c8f

def sum_pairs(ints, s):
    cache = set()
    for number in ints:
        if s - number in cache:
            return [s - number, number]
        cache.add(number)