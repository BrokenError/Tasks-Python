# https://www.codewars.com/kata/530e15517bc88ac656000716

def rot13(message):
    res= ''
    for i in message:
        if (ord(i) >= ord('A') and ord(i) <= ord('M')) or (ord(i) >= ord('a') and ord(i) <= ord('m')): res += chr(ord(i)+13)
        elif (ord(i) >= ord('N') and ord(i) <= ord('Z')) or (ord(i) >= ord('n') and ord(i) <= ord('z')): res += chr(ord(i)-13)
        else: res += i
    return res