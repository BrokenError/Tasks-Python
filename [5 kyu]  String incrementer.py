# https://www.codewars.com/kata/54a91a4883a7de5d7800009c


def increment_string(strng):
    letters = strng.rstrip('0123456789')
    numbers = strng[len(letters):]
    if numbers == '': return strng + '1'
    return letters + str(int(numbers)+1).zfill(len(numbers))