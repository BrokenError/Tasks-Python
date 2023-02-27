# https://www.codewars.com/kata/5412509bd436bd33920011bc

def maskify(cc):
    result = ""
    if len(cc) <= 4:
        return cc
    else:
        result += "#"*(len(cc)-4) + "".join([cc[i] for i in range(len(cc)-4, len(cc))])
        return result