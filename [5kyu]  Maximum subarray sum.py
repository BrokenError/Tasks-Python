# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def max_sequence(arr):
    sum = 0
    max_sum = 0
    for i in arr:
        sum += i
        max_sum = max(max_sum, sum)
        if sum < 0:
            sum = 0
    return max_sum