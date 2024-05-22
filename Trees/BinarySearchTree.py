class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    '''This constructor creates an empty binary search tree. The alternative would be to create the tree with the first node, this alternative version will be below'''
    def __init__(self):
        self.root = None
'''  
class BinarySearchTree():
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node
        self.length = 1
'''   
        
