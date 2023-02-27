# https://www.codewars.com/kata/550f22f4d758534c1100025a

def dirReduc(arr):
    for i in range(len(arr)-1):
        if {"SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST", "NORTH": "SOUTH"}[arr[i]] == arr[i+1]:
            del arr[i:i+2]
            return dirReduc(arr)
    return arr