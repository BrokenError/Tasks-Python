def duplicate_count(text):
    result = 0
    counter = {}
    
    for elem in list(text.lower()) :
        counter[elem] = counter.get(elem, 0) + 1
    
    for i, val in counter.items():
        print(i, val)
        if val >= 2:
            result+=1
    return result
