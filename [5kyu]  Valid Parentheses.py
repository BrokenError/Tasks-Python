# https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):    
    stack = []
    for s in string:
        if(s == '('):
            stack.append(s)
        elif(s == ')'):
            try:
                stack.pop()
            except:
                return False

    if(len(stack) == 0):
        return True
    else:
        return False