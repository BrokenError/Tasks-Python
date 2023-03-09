def alphabet_position(text):
    return ' '.join(str(ord(i) - ord('a') + 1) for i in text.lower() if i.isalpha())