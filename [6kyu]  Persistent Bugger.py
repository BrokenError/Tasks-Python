# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    if n < 10:
        return 0
    count = 1
    for i in str(n):
        count *= int(i)
    return 1 + persistence(count)