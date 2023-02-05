def zeros(n):
    count, i = 0, 5
    while n // i:
        count, i = count + n // i, i * 5
    return count