# https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(sequence):
    result = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i-1]:
            result.append(sequence[i])
    return result