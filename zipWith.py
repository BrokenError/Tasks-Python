def zip_with(fn,a1,a2):
    res = []
    for i in range(min(len(a1), len(a2))):
        res.append(fn(a1[i], a2[i]))
    return res