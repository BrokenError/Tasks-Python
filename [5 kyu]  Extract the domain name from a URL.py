# https://www.codewars.com/kata/514a024011ea4fb54200004b

def domain_name(url):
    url = url.replace('https://', '').replace('www.', '').replace('http://', '')
    return url.split('.')[0]