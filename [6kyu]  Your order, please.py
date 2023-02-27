# https://www.codewars.com/kata/55c45be3b2079eccff00010f

import re


def order(sentence):
    res = ' '.join(sorted(sentence.split(), key=lambda x: int(re.sub(r'.*?(\d+).*', r'\1', x+'_99999'))))
    return res