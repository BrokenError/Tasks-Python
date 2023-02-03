class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
def push(head, data):
    return Node(data, head)
  
def build_one_two_three():
    return push(push(push(None, 3), 2), 1)