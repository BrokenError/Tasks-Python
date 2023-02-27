# https://www.codewars.com/kata/583a02740b0a9fdf5900007c

def calc_fuel(n):
    set = {'lava': n*11 // 800}
    n = n*11%800
    set.update({'blaze rod': n // 120})
    n = n%120
    set.update({'coal': n // 80})
    n = n%80
    set.update({'wood': n // 15})
    n = n%15
    set.update({'stick': n})
    return set