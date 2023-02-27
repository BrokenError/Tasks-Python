# https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    res = ''
    for i in s.split():
        res += i.title()
    return False if len(res) > 140 or len(res) == 0 else '#' +  res