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
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while (True):
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    else:
                        temp = temp.left 
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    else:
                        temp = temp.right
       
            
        
my_b_search = BinarySearchTree()
my_b_search.insert(12)
my_b_search.insert(23)
my_b_search.insert(56)

            
        
