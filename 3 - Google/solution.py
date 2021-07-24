class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root is None:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))
    

def deserialize(stringed_tree):
    def createNode():
        actual = next(spt_values) #call each time the next value into string splitted tree
        if actual == '#':
            return None
        node = Node(actual)
        node.left = createNode()
        node.right = createNode()
        return node


    splitted_string_tree = stringed_tree.split()
    spt_values = iter(splitted_string_tree) #use the iter element to scan each value with next statement
    
        
    return createNode()
#O(N) Time
#O(N) space
def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

main()