# https://www.codewars.com/kata/5839edaa6754d6fec10000a2

def find_missing_letter(chars):
    word = ord(chars[0])
    for i in range(1, len(chars)):
        if word+1 != ord(chars[i]):
            return chr(word+1)
        else:
            word = ord(chars[i])