def what_century(year):
    year_list = list(year)
    century = (int(year)  - 1)  // 100 + 1
    if century%10 == 1 and century > 19:  
        return f"{century}st"
    elif century%10 == 2 and century > 19:
        return f"{century}nd"
    elif century%10 == 3 and century > 19:
        return f"{century}rd"
    else:
        return f"{century}th"