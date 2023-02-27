# https://www.codewars.com/kata/52bef5e3588c56132c0003bc

def tree_iterator(node: Node):
    nodes = [node]
    while nodes:
        yield from nodes
        for n in nodes[:]:
            if n.left: nodes.append(n.left)
            if n.right: nodes.append(n.right)
            nodes.remove(n)

            
def tree_by_levels(node):
    return [n.value for n in tree_iterator(node)] if node else []