# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def solution(strng,markers):
    res = strng.split('\n')
    for i in range(len(res)):
        s = res[i]
        for j in markers:
            index = s.find(j)
            if index >= 0:
                s = s[:index].rstrip()
        res[i] = s
    return '\n'.join(res)