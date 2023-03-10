# https://www.codewars.com/kata/559a28007caad2ac4e000083

def perimeter(k):
    series=[1,1]
    [series.append(series[k-1]+series[k-2]) for k in range(2,k+1)]
    return 4*sum(series)