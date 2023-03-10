# https://www.codewars.com/kata/54b724efac3d5402db00065e

from preloaded import MORSE_CODE

def decode_morse(morse_code):
    return ' '.join(''.join(MORSE_CODE[i] for i in word.split()) for word in morse_code.strip().split('   '))