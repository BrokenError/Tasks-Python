def find_outlier(integers):
    add = 0
    even = 0
    for i in integers[:3]:
        if i%2 != 0:
            add +=1
        else:
            even += 1
            
    if add > even:
        return [i for i in integers if i%2==0][0]
    else:
        return [i for i in integers if i%2!=0][0]