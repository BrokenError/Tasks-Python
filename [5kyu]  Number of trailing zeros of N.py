# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

def zeros(n):
    count, i = 0, 5
    while n // i:
        count, i = count + n // i, i * 5
    return count