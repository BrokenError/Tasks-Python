def sum_pairs(ints, s):
    cache = set()
    for number in ints:
        if s - number in cache:
            return [s - number, number]
        cache.add(number)