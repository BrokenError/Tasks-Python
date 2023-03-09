def narcissistic( value ):
    sum = 0
    count = len(str(value))
    for i in str(value):
        sum += int(i) **  count
    return sum == value