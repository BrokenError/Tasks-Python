def unique_in_order(sequence):
    result = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i-1]:
            result.append(sequence[i])
    return result