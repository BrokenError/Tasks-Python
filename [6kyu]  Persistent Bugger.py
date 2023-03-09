def persistence(n):
    if n < 10:
        return 0
    count = 1
    for i in str(n):
        count *= int(i)
    return 1 + persistence(count)