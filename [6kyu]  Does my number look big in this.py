# https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic( value ):
    sum = 0
    count = len(str(value))
    for i in str(value):
        sum += int(i) **  count
    return sum == value