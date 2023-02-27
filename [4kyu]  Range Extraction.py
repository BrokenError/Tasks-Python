# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(args):
    result = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                result.append( str(beg) )
            elif end == beg + 1:
                result.extend( [str(beg), str(end)] )
            else:
                result.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(result)