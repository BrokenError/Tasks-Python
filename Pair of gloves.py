def number_of_pairs(gloves):
    pairs = 0
    pair = ""
    gloves = sorted(gloves)
    print(gloves)
    for i in range(len(gloves)):
        if pair != gloves[i] or pair == "":
            pairs += (gloves.count(gloves[i]))//2
            pair = gloves[i]
    return pairs