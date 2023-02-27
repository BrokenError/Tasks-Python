# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    num = lst.count(0)
    return list(filter(lambda num: num != 0, lst)) + [0 for i in range(num)]