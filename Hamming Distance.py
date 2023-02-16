def hamming(a,b):
    diffs = 0
    prevMin=None
    if len(a) != len(b):
        return max(len(a),len(b))
    for ch1, ch2 in zip(a, b):
        if ch1 != ch2:
            diffs += 1
            if prevMin is not None and diffs>prevMin:
                return None
    return diffs 